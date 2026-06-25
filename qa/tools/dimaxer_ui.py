"""
Resolve ImGui paths via qa/tools/ui_path_registry.json (alias -> ImGui ref).

When tests live under qa/TestCase/<Case>/, import this module from qa/tools (see PythonTestRunner sys.path).
"""

from __future__ import annotations

from pathlib import Path
from typing import Union

import imgui_test_engine as te

from registry_resolver import RegistryResolver

_TOOLS_DIR = Path(__file__).resolve().parent
_resolver = RegistryResolver(_TOOLS_DIR / "ui_path_registry.json")

# Default poll window for WaitUntilItemExists (seconds).
_DEFAULT_WAIT_TIMEOUT_SEC = 15.0

# ImGuiTestOpFlags_NoError — query without marking the test context as errored.
_IMGUI_TEST_OP_NO_ERROR = 4
# ImGuiTestOpFlags_NoCheckHoveredId — RenderView1 (VTK ImageWithBg) is not ItemHoverable.
_IMGUI_TEST_OP_NO_CHECK_HOVERED = 2
# ImGuiTestOpFlags_NoFocusWindow
_IMGUI_TEST_OP_NO_FOCUS_WINDOW = 8
# Default flags for moving/dragging inside a Post render viewport.
RENDERVIEW_MOUSE_FLAGS = _IMGUI_TEST_OP_NO_FOCUS_WINDOW | _IMGUI_TEST_OP_NO_CHECK_HOVERED
_PROGRESS_IDLE_CONFIRM_FRAMES = 3

# After import, wait for this ribbon entry as "scene tree ready" marker.
_SCENE_READY_MESH_ALIAS = "post.ribbon.mesh_select_19"
_SCENE_READY_TIMEOUT_SEC = 60.0

Ref = Union[str, int]


def _ref(alias: str) -> str:
    return _resolver.require_ref(alias)


def _item_id(ref: Ref, flags: int = _IMGUI_TEST_OP_NO_ERROR) -> int:
    if isinstance(ref, str):
        info = te.ItemInfoOpenFullPath(ref, flags)
    else:
        info = te.ItemInfo(ref, flags)
    return int(info.get("id", 0) or 0)


def has_progress_bar() -> bool:
    """Return True if ProgressBar task is active (requires rebuilt host with IsProgressBarActive)."""
    is_active = getattr(te, "IsProgressBarActive", None)
    if is_active is None:
        raise RuntimeError(
            "imgui_test_engine.IsProgressBarActive missing: rebuild ImFramework (PythonTestRunner)."
        )
    return bool(is_active())


def any_progress_visible() -> bool:
    """Alias of has_progress_bar()."""
    return has_progress_bar()


def wait_until_progress_idle(*, confirm_frames: int = _PROGRESS_IDLE_CONFIRM_FRAMES) -> None:
    """Yield frames until ProgressBar is idle (must use Test Engine Yield, not Sleep(0))."""
    wait_fn = getattr(te, "WaitUntilProgressIdle", None)
    if wait_fn is not None:
        wait_fn(confirm_frames)
        return
    # Fallback for older host: Yield each frame (Sleep(0) does not yield in Normal run speed).
    yield_fn = getattr(te, "Yield", None)
    if yield_fn is None:
        raise RuntimeError(
            "imgui_test_engine.WaitUntilProgressIdle/Yield missing: rebuild ImFramework."
        )
    idle_streak = 0
    while idle_streak < confirm_frames:
        if has_progress_bar():
            idle_streak = 0
        else:
            idle_streak += 1
        yield_fn(1)


def wait_ui_idle() -> None:
    wait_until_progress_idle()


def wait_progress_bars_gone() -> None:
    wait_ui_idle()


def _wait_before_interact() -> None:
    wait_until_progress_idle()


def _yield_one_frame() -> None:
    yield_fn = getattr(te, "Yield", None)
    if yield_fn is not None:
        yield_fn(1)
    else:
        te.Sleep(0.1)


def wait_alias(
    alias: str,
    timeout_sec: float = _DEFAULT_WAIT_TIMEOUT_SEC,
) -> None:
    """Wait until alias resolves to a visible ImGui item (no click)."""
    _wait_before_interact()
    _ensure_exists(_ref(alias), alias=alias, timeout_sec=timeout_sec, skip_progress_wait=True)


def _poll_item_exists(ref: Ref, timeout_sec: float, poll_sec: float) -> bool:
    wait = getattr(te, "WaitUntilItemExists", None)
    if wait is not None:
        return bool(wait(ref, timeout_sec))
    elapsed = 0.0
    while elapsed < timeout_sec:
        if _item_id(ref) != 0:
            return True
        te.Sleep(poll_sec)
        elapsed += poll_sec
    return _item_id(ref) != 0


def _ensure_exists(
    ref: Ref,
    *,
    alias: str | None = None,
    timeout_sec: float = _DEFAULT_WAIT_TIMEOUT_SEC,
    skip_progress_wait: bool = False,
) -> None:
    """Wait for control; waits for progress popups to close first unless already done."""
    if not skip_progress_wait:
        _wait_before_interact()

    if _poll_item_exists(ref, timeout_sec, 0.1):
        return

    # One retry after UI settles (panel open / tree refresh).
    _yield_one_frame()
    _wait_before_interact()
    if _poll_item_exists(ref, timeout_sec, 0.1):
        return

    if alias is None:
        raise RuntimeError(f"ItemNotFound ref={ref!r} (timed out after {timeout_sec}s)")
    raise RuntimeError(f"ItemNotFound alias={alias!r} ref={ref!r} (timed out after {timeout_sec}s)")


def _drain_progress_after_action() -> None:
    if has_progress_bar():
        wait_until_progress_idle()


def item_click(
    alias: str,
    mouse_action: int = 0,
    flags: int = 0,
) -> None:
    ref = _ref(alias)
    _ensure_exists(ref, alias=alias)
    te.ItemClick(ref, mouse_action, flags)
    _yield_one_frame()
    _drain_progress_after_action()


def wait_post_apply_done() -> None:
    """Wait until Post Apply progress finishes."""
    wait_until_progress_idle()


def wait_enter_post_done() -> None:
    """Wait until Enter Post progress finishes (after ImportModelPost)."""
    wait_until_progress_idle()


def wait_progress_done(title: str) -> None:
    """Wait until progress finishes (title ignored; uses active-state polling)."""
    del title
    wait_until_progress_idle()


def select_view_ribbon_tab() -> None:
    """Switch to View ribbon tab (C++ scroll + changeTab_; do not use ItemClick on ##ViewTabId)."""
    fn = getattr(te, "PrepareRibbonViewTab", None)
    if fn is None:
        raise RuntimeError(
            "imgui_test_engine.PrepareRibbonViewTab missing: rebuild ImFramework (PythonTestRunner)."
        )
    fn()
    _yield_one_frame()


def select_post_ribbon_tab() -> None:
    """Switch to Post ribbon tab and post mode (same as runner preparePythonTest_PostTab)."""
    fn = getattr(te, "PrepareRibbonPostTab", None)
    if fn is None:
        raise RuntimeError(
            "imgui_test_engine.PrepareRibbonPostTab missing: rebuild ImFramework (PythonTestRunner)."
        )
    fn()
    _yield_one_frame()


def import_model_post(
    model_path: str,
    *,
    wait_enter_post: bool = True,
) -> None:
    """Import model, enter Post, wait for progress and scene-tree ready marker."""
    te.ImportModelPost(model_path)
    if wait_enter_post:
        wait_enter_post_done()
    wait_ui_idle()
    wait_alias(_SCENE_READY_MESH_ALIAS, _SCENE_READY_TIMEOUT_SEC)


def import_csv_file(csv_path: str) -> None:
    """Import a CSV via Post Open files, without using Solution Loader/Apply."""
    path = Path(csv_path)
    if not path.is_absolute():
        path = Path(te.GetWorkSpacePath()) / "Model" / path

    select_post_ribbon_tab()
    item_click("post.top.open_files", 0, _IMGUI_TEST_OP_NO_FOCUS_WINDOW)
    item_input_value("post.dialog.open_file_input", str(path))
    wait_ui_idle()
    
def ribbon_hide_all_and_select_mesh(mesh_alias: str = _SCENE_READY_MESH_ALIAS) -> None:
    """Hide all visibility, wait for progress, then select mesh (tree ready)."""
    wait_progress_bars_gone()
    item_click("post.ribbon.hide_all", 0, 8)
    wait_progress_bars_gone()
    item_click(mesh_alias)


def item_click_apply(
    alias: str,
    mouse_action: int = 0,
    flags: int = 0,
) -> None:
    """Click a Post Apply alias, then wait for Process Model progress to finish."""
    item_click(alias, mouse_action, flags)
    wait_post_apply_done()


def item_click_ref(ref: str, mouse_action: int = 0, flags: int = 0) -> None:
    _ensure_exists(ref)
    te.ItemClick(ref, mouse_action, flags)
    _yield_one_frame()
    _drain_progress_after_action()


def item_click_ref_apply(
    ref: str,
    mouse_action: int = 0,
    flags: int = 0,
) -> None:
    """Click a raw ImGui ref (e.g. Postbug ContentTable/Apply), then wait for Process Model."""
    item_click_ref(ref, mouse_action, flags)
    wait_post_apply_done()


def item_click_id(item_id: int, mouse_action: int = 0, flags: int = 0) -> None:
    _ensure_exists(item_id)
    te.ItemClick(item_id, mouse_action, flags)
    _yield_one_frame()
    _drain_progress_after_action()


def tab_close_ref(ref: str) -> None:
    """Close tab via te.TabClose (stable vs per-tab #CLOSE paths)."""
    _wait_before_interact()
    fn = getattr(te, "TabClose", None)
    if fn is None:
        raise RuntimeError(
            "imgui_test_engine.TabClose missing: rebuild host (PythonTestRunner exports TabClose)."
        )
    fn(ref)


def tab_close(alias: str) -> None:
    tab_close_ref(_ref(alias))


def combo_click(alias: str, item_label: str) -> None:
    ref = _ref(alias)
    _ensure_exists(ref, alias=alias)
    te.ComboClick(ref, item_label)
    _yield_one_frame()
    _drain_progress_after_action()


def combo_click_ref(ref: str, item_label: str) -> None:
    _ensure_exists(ref)
    te.ComboClick(ref, item_label)
    _yield_one_frame()
    _drain_progress_after_action()


def _compare_last_capture(
    baseline: str,
    actual: str,
    *,
    threshold: float = 0.99,
    wait_seconds: float = 1.0,
) -> bool:
    from compare_images_ssim import compare_images

    ok, detail = compare_images(baseline, actual, threshold=threshold, wait_seconds=wait_seconds)
    report_fn = getattr(te, "ReportCaptureCompareResult", None)
    if report_fn is None:
        raise RuntimeError(
            "imgui_test_engine.ReportCaptureCompareResult missing: rebuild ImFramework (PythonTestRunner)."
        )
    report_fn(ok, baseline, actual, detail)
    if not ok:
        raise RuntimeError(f"Capture image compare failed: {baseline} vs {actual}")
    return ok


def capture_renderview(flags: int = 8, window: str = "renderview1") -> None:
    """Capture a RenderView window and compare to baseline.

    window: registry alias suffix (default renderview1 -> post.renderview1),
    or a full alias when it already starts with post.
    """
    alias = window if window.startswith("post.") else f"post.{window}"
    capture_window(alias, flags)


def capture_renderview_ref(ref: str, flags: int = 8) -> None:
    _ensure_exists(ref)
    baseline, actual = te.CaptureScreenshotWindow(ref, flags)
    _compare_last_capture(baseline, actual)


def item_input_value(alias: str, value) -> None:
    ref = _ref(alias)
    _ensure_exists(ref, alias=alias)
    te.ItemInputValue(ref, value)
    _yield_one_frame()
    _drain_progress_after_action()


def item_input_value_ref(ref: str, value) -> None:
    _ensure_exists(ref)
    te.ItemInputValue(ref, value)
    _yield_one_frame()
    _drain_progress_after_action()


def item_read_float(alias: str) -> float:
    """Read numeric value from InputFloat/DragFloat (requires ItemReadAsFloat in host)."""
    ref = _ref(alias)
    _ensure_exists(ref, alias=alias)
    read_fn = getattr(te, "ItemReadAsFloat", None)
    if read_fn is None:
        raise RuntimeError(
            "imgui_test_engine.ItemReadAsFloat missing: rebuild ImFramework (PythonTestRunner)."
        )
    return float(read_fn(ref))


def item_read_string(alias: str) -> str:
    ref = _ref(alias)
    _ensure_exists(ref, alias=alias)
    return item_read_string_ref(ref)


def item_read_string_ref(ref: str) -> str:
    _ensure_exists(ref)
    read_fn = getattr(te, "ItemReadAsString", None)
    if read_fn is None:
        raise RuntimeError(
            "imgui_test_engine.ItemReadAsString missing: rebuild ImFramework (PythonTestRunner)."
        )
    te.ItemClick(ref)
    _yield_one_frame()
    return str(read_fn(ref))


def item_is_checked(alias: str) -> bool:
    ref = _ref(alias)
    _ensure_exists(ref, alias=alias)
    fn = getattr(te, "ItemIsChecked", None)
    if fn is None:
        raise RuntimeError(
            "imgui_test_engine.ItemIsChecked missing: rebuild ImFramework (PythonTestRunner)."
        )
    return bool(fn(ref))


def item_double_click(alias: str, flags: int = 0) -> None:
    ref = _ref(alias)
    _ensure_exists(ref, alias=alias)
    te.ItemDoubleClick(ref, flags)
    _yield_one_frame()
    _drain_progress_after_action()


def item_double_click_ref(ref: str, flags: int = 0) -> None:
    _ensure_exists(ref)
    te.ItemDoubleClick(ref, flags)
    _yield_one_frame()
    _drain_progress_after_action()


def scroll_to_bottom(alias: str) -> None:
    ref = _ref(alias)
    _ensure_exists(ref, alias=alias)
    te.ScrollToBottom(ref)


def scroll_to_bottom_ref(ref: str) -> None:
    _ensure_exists(ref)
    te.ScrollToBottom(ref)


def scroll_to_top(alias: str) -> None:
    ref = _ref(alias)
    _ensure_exists(ref, alias=alias)
    te.ScrollToTop(ref)


def scroll_to_top_ref(ref: str) -> None:
    _ensure_exists(ref)
    te.ScrollToTop(ref)


def _renderview_mouse_flags(ref: str, flags: int) -> int:
    """RenderView hosts VTK; ImGui hover id often won't match even when the pointer is over the viewport."""
    tail = ref.rsplit("/", 1)[-1]
    if tail == "RenderView1" or tail.startswith("RenderView"):
        return flags | _IMGUI_TEST_OP_NO_CHECK_HOVERED
    return flags


def mouse_move(alias: str, flags: int = 0) -> None:
    ref = _ref(alias)
    _ensure_exists(ref, alias=alias)
    te.MouseMove(ref, _renderview_mouse_flags(ref, flags))


def mouse_move_renderview(flags: int = RENDERVIEW_MOUSE_FLAGS) -> None:
    """Move mouse into RenderView1 (for VTK rotate/pan via MouseDragWithDelta)."""
    mouse_move("post.renderview1", flags)


def mouse_move_ref(ref: str, flags: int = 0) -> None:
    _ensure_exists(ref)
    te.MouseMove(ref, _renderview_mouse_flags(ref, flags))


def capture_window(alias: str, flags: int = 8) -> None:
    ref = _ref(alias)
    _ensure_exists(ref, alias=alias)
    baseline, actual = te.CaptureScreenshotWindow(ref, flags)
    _compare_last_capture(baseline, actual)


def capture_window_ref(ref: str, flags: int = 8) -> None:
    _ensure_exists(ref)
    baseline, actual = te.CaptureScreenshotWindow(ref, flags)
    _compare_last_capture(baseline, actual)


def require_ref(alias: str) -> str:
    """Resolved ImGui path for alias (from ui_path_registry.json)."""
    return _ref(alias)


def alias_exists_now(alias: str) -> bool:
    """Single-frame existence check; no wait loop and no LogError when missing."""
    return _item_id(_ref(alias)) != 0


def gather_items(parent_ref: str, depth: int = -1) -> list[dict]:
    """Gather ImGui items under parent_ref.

    Each dict includes id/debug_label/window_name and, after ImFramework rebuild,
    ``ref`` (decorated ImGui path suitable for ui_path_registry.json).
    """
    gather = getattr(te, "GatherItems", None)
    if gather is None:
        raise RuntimeError(
            "imgui_test_engine.GatherItems missing: rebuild ImFramework (PythonTestRunner)."
        )
    return list(gather(parent_ref, depth))


def gather_scene_tree_items(depth: int = -1) -> list[dict]:
    """Gather Post scene tree (RibbonScene Meshes); items include ``ref`` when host is rebuilt."""
    return gather_items("//RibbonScene", depth)


def fetch_snapshot(
    *,
    parent: str = "//RibbonScene",
    depth: int = -1,
    scene_tree_only: bool = True,
    registry_candidates_only: bool = True,
    base_url: str = "http://127.0.0.1:17862",
    poll_timeout_sec: float = 30.0,
) -> list[dict]:
    """POST /snapshot then poll until ready (Collab QA HTTP API; requires rebuilt ImFramework)."""
    import json
    import time
    import urllib.error
    import urllib.request

    body = json.dumps(
        {
            "parent": parent,
            "depth": depth,
            "scene_tree_only": scene_tree_only,
            "registry_candidates_only": registry_candidates_only,
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        f"{base_url.rstrip('/')}/snapshot",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        job_id = int(json.load(resp)["job_id"])

    deadline = time.monotonic() + poll_timeout_sec
    while time.monotonic() < deadline:
        poll_req = urllib.request.Request(f"{base_url.rstrip('/')}/snapshot/{job_id}", method="GET")
        with urllib.request.urlopen(poll_req, timeout=10) as resp:
            payload = json.load(resp)
        if payload.get("ready"):
            if payload.get("error"):
                raise RuntimeError(f"snapshot job {job_id} failed: {payload['error']}")
            return list(payload.get("items") or [])
        time.sleep(0.3)
    raise TimeoutError(f"snapshot job {job_id} not ready after {poll_timeout_sec}s")

