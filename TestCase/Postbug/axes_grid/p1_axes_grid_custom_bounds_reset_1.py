import dimaxer_ui as ui

_X0 = 3.0
_X1 = 2.0
_Y0 = 1.0
_Y1 = 2.0
_Z0 = 4.0
_Z1 = 5.0

_EDIT_ROW_SUFFIX = "/$$0/##edit"


def _alias_exists(alias: str, timeout_sec: float = 0.5) -> bool:
    try:
        ui.wait_alias(alias, timeout_sec=timeout_sec)
        return True
    except RuntimeError:
        return False


def _ensure_checked(alias: str) -> None:
    ui.wait_alias(alias, timeout_sec=15.0)
    if not ui.item_is_checked(alias):
        ui.item_click(alias, 0, 8)
        ui.wait_ui_idle()


def _scroll_axes_modal_to_top() -> None:
    if _alias_exists("post.axes_grid.modal", 2.0):
        ui.scroll_to_top("post.axes_grid.modal")
        ui.wait_ui_idle()


def _scroll_axes_modal_to_bottom() -> None:
    """弹窗禁用了滚动条，XYZ 都展开后底部 Reset/Close 在视口外，需滚到底再点。"""
    if _alias_exists("post.axes_grid.modal", 2.0):
        ui.scroll_to_bottom("post.axes_grid.modal")
        ui.wait_ui_idle()


def _editor_table_parent(axis: str) -> str:
    """RowEditor 列表区（####m_AxeseditorN），不含 $$i/##edit 行。"""
    row_ref = ui.require_ref(f"post.axes_grid.{axis}_edit_0")
    if not row_ref.endswith(_EDIT_ROW_SUFFIX):
        raise RuntimeError(f"unexpected edit_0 ref for {axis}: {row_ref!r}")
    return row_ref[: -len(_EDIT_ROW_SUFFIX)]


def _count_custom_bound_edits(axis: str) -> int:
    """统计该轴 RowEditor 下 InputFloat(##edit) 行数；勿用 WaitUntilItemExists（不存在也会 LogError）。"""
    items = ui.gather_items(_editor_table_parent(axis), 3)
    return sum(1 for item in items if item.get("debug_label") == "##edit")


def _assert_no_residual_rows(axis: str) -> None:
    ui.wait_ui_idle()
    count = _count_custom_bound_edits(axis)
    if count > 0:
        raise RuntimeError(
            f"post.axes_grid.{axis} has {count} custom bound edit row(s) after Reset, expected 0"
        )


def p1_axes_grid_custom_bounds_reset_1():
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.scene.advanced_options", 0, 8)
    ui.scroll_to_bottom("post.scene.properties_scroll")
    ui.item_click("post.scene.axes_grid_open", 0, 8)
    ui.wait_alias("post.axes_grid.x_use_custom_bounds")

    _ensure_checked("post.axes_grid.x_use_custom_bounds")
    ui.item_click("post.axes_grid.x_plus", 0, 8)
    ui.item_click("post.axes_grid.x_plus", 0, 8)
    ui.item_input_value("post.axes_grid.x_edit_0", _X0)
    ui.item_input_value("post.axes_grid.x_edit_1", _X1)

    _ensure_checked("post.axes_grid.y_use_custom_bounds")
    ui.item_click("post.axes_grid.y_plus", 0, 8)
    ui.item_click("post.axes_grid.y_plus", 0, 8)
    ui.item_input_value("post.axes_grid.y_edit_0", _Y0)
    ui.item_input_value("post.axes_grid.y_edit_1", _Y1)
    _scroll_axes_modal_to_bottom()

    _ensure_checked("post.axes_grid.z_use_custom_bounds")
    ui.item_click("post.axes_grid.z_plus", 0, 8)
    ui.item_click("post.axes_grid.z_plus", 0, 8)
    ui.item_input_value("post.axes_grid.z_edit_0", _Z0)
    ui.item_input_value("post.axes_grid.z_edit_1", _Z1)
    _scroll_axes_modal_to_bottom()

    ui.item_click("post.axes_grid.reset", 0, 8)
    ui.wait_ui_idle()
    ui.wait_alias("post.axes_grid.modal")

    _scroll_axes_modal_to_top()
    _ensure_checked("post.axes_grid.x_use_custom_bounds")
    _ensure_checked("post.axes_grid.y_use_custom_bounds")
    _scroll_axes_modal_to_bottom()
    _ensure_checked("post.axes_grid.z_use_custom_bounds")
    ui.wait_ui_idle()

    _scroll_axes_modal_to_top()
    _assert_no_residual_rows("x")
    _assert_no_residual_rows("y")
    _scroll_axes_modal_to_bottom()
    _assert_no_residual_rows("z")

    # 断言时临时勾选了 XYZ；逐轴 item_click 取消在弹窗内常因滚出视口点不到。
    # 再点一次底部 Reset，与第一次 Reset 相同，从 adapter 恢复未勾选/折叠。
    _scroll_axes_modal_to_bottom()
    ui.item_click("post.axes_grid.reset", 0, 8)
    ui.wait_ui_idle()


    ui.item_click("post.axes_grid.close", 0, 8)
    ui.item_click("post.scene.advanced_options", 0, 8)