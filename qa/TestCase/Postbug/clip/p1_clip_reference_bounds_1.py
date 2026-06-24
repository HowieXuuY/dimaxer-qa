import dimaxer_ui as ui

_VALUE_EPS = 1e-3

_EXPECT_X0 = 34.0
_EXPECT_X1 = 33.0
_EXPECT_Y0 = 3.0
_EXPECT_Y1 = 14.0
_EXPECT_Z0 = 18.0
_EXPECT_Z1 = 37.0


def p1_clip_reference_bounds_1():
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.clip_panel", 0, 8)
    ui.combo_click("post.clip.combo_type", "Box")

    if not ui.item_is_checked("post.clip.ref_bounds"):
        ui.item_click("post.clip.ref_bounds", 0, 8)

    ui.item_input_value("post.clip.range_x0", _EXPECT_X0)
    ui.item_input_value("post.clip.range_x1", _EXPECT_X1)
    ui.item_input_value("post.clip.range_y0", _EXPECT_Y0)
    ui.item_input_value("post.clip.range_y1", _EXPECT_Y1)
    ui.item_input_value("post.clip.range_z0", _EXPECT_Z0)
    ui.item_input_value("post.clip.range_z1", _EXPECT_Z1)

    ui.wait_ui_idle()

    text = ui.item_read_string("post.clip.range_x0").strip()
    actual = float(text)
    if abs(actual - _EXPECT_X0) > _VALUE_EPS:
        raise RuntimeError(f"post.clip.range_x0 expected {_EXPECT_X0}, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.clip.range_x1").strip()
    actual = float(text)
    if abs(actual - _EXPECT_X1) > _VALUE_EPS:
        raise RuntimeError(f"post.clip.range_x1 expected {_EXPECT_X1}, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.clip.range_y0").strip()
    actual = float(text)
    if abs(actual - _EXPECT_Y0) > _VALUE_EPS:
        raise RuntimeError(f"post.clip.range_y0 expected {_EXPECT_Y0}, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.clip.range_y1").strip()
    actual = float(text)
    if abs(actual - _EXPECT_Y1) > _VALUE_EPS:
        raise RuntimeError(f"post.clip.range_y1 expected {_EXPECT_Y1}, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.clip.range_z0").strip()
    actual = float(text)
    if abs(actual - _EXPECT_Z0) > _VALUE_EPS:
        raise RuntimeError(f"post.clip.range_z0 expected {_EXPECT_Z0}, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.clip.range_z1").strip()
    actual = float(text)
    if abs(actual - _EXPECT_Z1) > _VALUE_EPS:
        raise RuntimeError(f"post.clip.range_z1 expected {_EXPECT_Z1}, got {actual!r} (text={text!r})")
