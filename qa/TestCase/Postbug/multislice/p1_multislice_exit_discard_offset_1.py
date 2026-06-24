import dimaxer_ui as ui

# C++: close/Exit → resetToolPanel；未 Apply 的 OffSet 草稿丢弃

_VALUE_EPS = 1e-3
_DRAFT_OFFSET = 9.0


def p1_multislice_exit_discard_offset_1():
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.multislice_panel", 0, 8)
    ui.wait_alias("post.multislice.input_offset")

    text = ui.item_read_string("post.multislice.input_offset").strip()
    before_exit = float(text)

    ui.item_input_value("post.multislice.input_offset", _DRAFT_OFFSET)
    ui.item_click("post.multislice.exit", 0, 8)
    ui.wait_ui_idle()

    ui.item_click("post.top.multislice_panel", 0, 8)
    ui.wait_alias("post.multislice.input_offset")

    text = ui.item_read_string("post.multislice.input_offset").strip()
    actual = float(text)
    if abs(actual - _DRAFT_OFFSET) <= _VALUE_EPS:
        raise RuntimeError(
            f"post.multislice.input_offset still {_DRAFT_OFFSET} after Exit; draft should be discarded"
        )
    if abs(actual - before_exit) > _VALUE_EPS:
        raise RuntimeError(
            f"post.multislice.input_offset expected {before_exit} after Exit+reopen, got {actual!r}"
        )
