import dimaxer_ui as ui

# 验证 Contour：Apply 后生成的 Value Setting 三行在 Exit 再打开后仍在；
# 未 Apply 的 Generate Number 草稿在 Exit 后应丢弃，已 Apply 的值应保留。

_VALUE_EPS = 1e-3
_APPLY_GENERATE_NUMBER = 3.0
_DISCARD_GENERATE_NUMBER = 0.0

_ROW_ALIASES = (
    "post.contour.roweditor_edit_r0",
    "post.contour.roweditor_edit_r1",
    "post.contour.roweditor_edit_r2",
)


def _read_generate_number() -> float:
    text = ui.item_read_string("post.contour.input_generate_number").strip()
    return float(text)


def _assert_generate_number(expected: float) -> None:
    actual = _read_generate_number()
    if abs(actual - expected) > _VALUE_EPS:
        raise RuntimeError(
            f"post.contour.input_generate_number expected {expected}, got {actual!r}"
        )


def _assert_value_rows_present() -> None:
    for alias in _ROW_ALIASES:
        ui.wait_alias(alias)
        value = ui.item_read_float(alias)
        if value != value:
            raise RuntimeError(f"{alias} is NaN after Exit+reopen")
        if abs(value) <= _VALUE_EPS:
            raise RuntimeError(f"{alias} expected non-zero contour value, got {value!r}")


def p1_contour_exit_reopen_rows_1():
    # 导入 Post 模型并选中默认 vol（mesh 19）
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    # 打开 Contour 面板，等待 Generate Number 输入框就绪
    ui.item_click("post.top.contour_panel", 0, 8)
    ui.wait_alias("post.contour.input_generate_number")

    # 将 Generate Number 设为 3 并确认输入生效（后续 Apply 会按此数量生成等值线行）
    ui.item_click("post.contour.input_generate_number", 0, 8)
    ui.item_input_value("post.contour.input_generate_number", _APPLY_GENERATE_NUMBER)
    _assert_generate_number(_APPLY_GENERATE_NUMBER)

    # Apply：生成 Contour 对象，场景树出现 mesh_contour1
    ui.item_click_apply("post.contour.apply", 0, 8)
    ui.wait_alias("post.ribbon.mesh_contour1", 30.0)

    # 双击场景树中的 Contour，打开编辑面板；检查 Value Setting 三行均有非零数值
    ui.item_double_click("post.ribbon.mesh_contour1", 8)
    ui.wait_alias("post.contour.input_generate_number")
    _assert_value_rows_present()

    # 把 Generate Number 改成 0（仅草稿，不点 Apply），点 Exit 关闭面板
    ui.item_click("post.contour.input_generate_number", 0, 8)
    ui.item_input_value("post.contour.input_generate_number", _DISCARD_GENERATE_NUMBER)
    ui.item_click("post.contour.exit", 0, 8)
    ui.wait_ui_idle()

    # 再次双击 Contour 打开面板：Generate Number 应仍为 Apply 时的 3（草稿 0 已丢弃）
    ui.item_double_click("post.ribbon.mesh_contour1", 8)
    ui.wait_alias("post.contour.input_generate_number")

    _assert_generate_number(_APPLY_GENERATE_NUMBER)
    # Value Setting 三行仍应存在且为非零（Apply 结果未被 Exit 清掉）
    _assert_value_rows_present()
