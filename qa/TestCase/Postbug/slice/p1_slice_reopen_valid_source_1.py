import dimaxer_ui as ui

# C++: InitToolBySelectEntity 成功后 Source 为父实体名；失败为 Please select...

_SOURCE_FAIL_MARKERS = (
    "Please select source from model tree",
    "Please select valid source from model tree",
)


def p1_slice_reopen_valid_source_1():
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.slice_panel", 0, 8)
    ui.wait_alias("post.slice.source_text")

    text = ui.item_read_string("post.slice.source_text").strip()
    for marker in _SOURCE_FAIL_MARKERS:
        if marker in text:
            raise RuntimeError(f"post.slice.source_text should show mesh source, got {text!r}")

    ui.item_click_apply("post.slice.apply", 0, 8)
    ui.wait_ui_idle()

    ui.item_click("post.top.slice_panel", 0, 8)
    ui.wait_alias("post.slice.source_text")

    text = ui.item_read_string("post.slice.source_text").strip()
    for marker in _SOURCE_FAIL_MARKERS:
        if marker in text:
            raise RuntimeError(
                f"post.slice.source_text should show mesh source after Apply+reopen, got {text!r}"
            )
