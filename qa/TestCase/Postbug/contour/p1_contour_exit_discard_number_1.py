import dimaxer_ui as ui

# C++: Exit 关 dialog；未 Apply 的 Generate Number 不应保留

_VALUE_EPS = 1e-3
_DRAFT = 99.0


def p1_contour_exit_discard_number_1():
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.contour_panel", 0, 8)
    ui.wait_alias("post.contour.input_generate_number")

    text = ui.item_read_string("post.contour.input_generate_number").strip()
    before_exit = float(text)

    ui.item_input_value("post.contour.input_generate_number", _DRAFT)
    ui.item_click("post.contour.exit", 0, 8)
    ui.wait_ui_idle()

    ui.item_click("post.top.contour_panel", 0, 8)
    ui.wait_alias("post.contour.input_generate_number")

    text = ui.item_read_string("post.contour.input_generate_number").strip()
    actual = float(text)
    if abs(actual - _DRAFT) <= _VALUE_EPS:
        raise RuntimeError(
            f"post.contour.input_generate_number still {_DRAFT} after Exit; draft should be discarded"
        )
    if abs(actual - before_exit) > _VALUE_EPS:
        raise RuntimeError(
            f"post.contour.input_generate_number expected {before_exit} after Exit+reopen, got {actual!r}"
        )
