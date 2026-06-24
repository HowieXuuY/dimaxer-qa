import dimaxer_ui as ui

_VALUE_EPS = 1e-3
_EXPECT_FIRST = 1.0
_EXPECT_SECOND = 2.0
#bug 链接
#https://project.feishu.cn/dimaxer-dev/issue/detail/6737456684

def p1_contour_generate_number_pressure_1():
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.contour_panel", 0, 8)

    ui.item_click("post.contour.input_generate_number", 0, 8)
    ui.item_input_value("post.contour.input_generate_number", _EXPECT_FIRST)
    ui.wait_ui_idle()

    text = ui.item_read_string("post.contour.input_generate_number").strip()
    actual = float(text)
    if abs(actual - _EXPECT_FIRST) > _VALUE_EPS:
        raise RuntimeError(
            f"Generate Number expected {_EXPECT_FIRST} before Quantity change, got {actual!r} (text={text!r})"
        )

    ui.combo_click("post.contour.combo_quantity", "Pressure")

    ui.item_click("post.contour.input_generate_number", 0, 8)
    ui.item_input_value("post.contour.input_generate_number", _EXPECT_SECOND)
    ui.wait_ui_idle()

    text = ui.item_read_string("post.contour.input_generate_number").strip()
    actual = float(text)
    if abs(actual - _EXPECT_SECOND) > _VALUE_EPS:
        raise RuntimeError(
            f"Generate Number expected {_EXPECT_SECOND} after Pressure + re-input, got {actual!r} (text={text!r})"
        )
