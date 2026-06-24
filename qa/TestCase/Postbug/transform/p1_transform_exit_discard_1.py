import dimaxer_ui as ui
#bug 链接
#https://project.feishu.cn/dimaxer-dev/issue/detail/6739521231
_VALUE_EPS = 1e-3

_APPLY_O0 = 12.0
_APPLY_O1 = 23.0
_APPLY_O2 = 12.0
_APPLY_R0 = 0.0
_APPLY_R1 = 0.0
_APPLY_R2 = 0.0

_DISCARD_O0 = 99.0
_DISCARD_O1 = 88.0
_DISCARD_O2 = 77.0


def p1_transform_exit_discard_1():
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.transform_panel", 0, 8)
    ui.combo_click("post.transform.combo_type", "RotateAroundOriginTransform")

    ui.item_input_value("post.transform.origin_0", _APPLY_O0)
    ui.item_input_value("post.transform.origin_1", _APPLY_O1)
    ui.item_input_value("post.transform.origin_2", _APPLY_O2)
    ui.item_input_value("post.transform.rotate_0", _APPLY_R0)
    ui.item_input_value("post.transform.rotate_1", _APPLY_R1)
    ui.item_input_value("post.transform.rotate_2", _APPLY_R2)

    ui.item_click_apply("post.transform.apply", 0, 8)
    ui.wait_ui_idle()

    ui.item_double_click("post.ribbon.mesh_pvtransform1", 8)
    ui.wait_alias("post.transform.origin_0")

    ui.item_input_value("post.transform.origin_0", _DISCARD_O0)
    ui.item_input_value("post.transform.origin_1", _DISCARD_O1)
    ui.item_input_value("post.transform.origin_2", _DISCARD_O2)

    ui.item_click("post.transform.exit", 0, 8)
    ui.wait_ui_idle()

    ui.item_double_click("post.ribbon.mesh_pvtransform1", 8)
    ui.wait_alias("post.transform.origin_0")

    text = ui.item_read_string("post.transform.origin_0").strip()
    actual = float(text)
    if abs(actual - _APPLY_O0) > _VALUE_EPS:
        raise RuntimeError(f"origin_0 expected {_APPLY_O0} after Exit, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.transform.origin_1").strip()
    actual = float(text)
    if abs(actual - _APPLY_O1) > _VALUE_EPS:
        raise RuntimeError(f"origin_1 expected {_APPLY_O1} after Exit, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.transform.origin_2").strip()
    actual = float(text)
    if abs(actual - _APPLY_O2) > _VALUE_EPS:
        raise RuntimeError(f"origin_2 expected {_APPLY_O2} after Exit, got {actual!r} (text={text!r})")

    text = ui.item_read_string("post.transform.rotate_0").strip()
    actual = float(text)
    if abs(actual - _APPLY_R0) > _VALUE_EPS:
        raise RuntimeError(f"rotate_0 expected {_APPLY_R0} after Exit, got {actual!r} (text={text!r})")
