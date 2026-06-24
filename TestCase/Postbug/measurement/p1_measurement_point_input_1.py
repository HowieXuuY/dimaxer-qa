import dimaxer_ui as ui

_VALUE_EPS = 1e-4

_EXPECT_P1X = 0.5
_EXPECT_P1Y = 0.5
_EXPECT_P1Z = 0.2
_EXPECT_P2X = 0.3
_EXPECT_P2Y = 0.1
_EXPECT_P2Z = 0.6


def p1_measurement_point_input_1():
    ui.item_click("post.quickaccess.measurement", 0, 8)
    ui.wait_alias("post.measurement.point1_x", timeout_sec=30.0)

    ui.item_double_click("post.measurement.point1_x", 8)
    ui.item_input_value("post.measurement.point1_x", _EXPECT_P1X)
    ui.item_double_click("post.measurement.point1_y", 8)
    ui.item_input_value("post.measurement.point1_y", _EXPECT_P1Y)
    ui.item_double_click("post.measurement.point1_z", 8)
    ui.item_input_value("post.measurement.point1_z", _EXPECT_P1Z)

    ui.item_double_click("post.measurement.point2_x", 8)
    ui.item_input_value("post.measurement.point2_x", _EXPECT_P2X)
    ui.item_double_click("post.measurement.point2_y", 8)
    ui.item_input_value("post.measurement.point2_y", _EXPECT_P2Y)
    ui.item_double_click("post.measurement.point2_z", 8)
    ui.item_input_value("post.measurement.point2_z", _EXPECT_P2Z)

    ui.wait_ui_idle()

    text = ui.item_read_string("post.measurement.point1_x").strip()
    actual = float(text)
    if abs(actual - _EXPECT_P1X) > _VALUE_EPS:
        raise RuntimeError(f"post.measurement.point1_x expected {_EXPECT_P1X}, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.measurement.point1_y").strip()
    actual = float(text)
    if abs(actual - _EXPECT_P1Y) > _VALUE_EPS:
        raise RuntimeError(f"post.measurement.point1_y expected {_EXPECT_P1Y}, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.measurement.point1_z").strip()
    actual = float(text)
    if abs(actual - _EXPECT_P1Z) > _VALUE_EPS:
        raise RuntimeError(f"post.measurement.point1_z expected {_EXPECT_P1Z}, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.measurement.point2_x").strip()
    actual = float(text)
    if abs(actual - _EXPECT_P2X) > _VALUE_EPS:
        raise RuntimeError(f"post.measurement.point2_x expected {_EXPECT_P2X}, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.measurement.point2_y").strip()
    actual = float(text)
    if abs(actual - _EXPECT_P2Y) > _VALUE_EPS:
        raise RuntimeError(f"post.measurement.point2_y expected {_EXPECT_P2Y}, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.measurement.point2_z").strip()
    actual = float(text)
    if abs(actual - _EXPECT_P2Z) > _VALUE_EPS:
        raise RuntimeError(f"post.measurement.point2_z expected {_EXPECT_P2Z}, got {actual!r} (text={text!r})")
