import imgui_test_engine as te

import dimaxer_ui as ui

# PostTests：Threshold 功能回归（默认 dmh vol 19，截图比对渲染视图）。
# Apply 后隐藏源 vol，避免与过滤结果重叠。

# Density Between（DefaultThreshold）
_THRESHOLD_LOWER = 1.140
_THRESHOLD_UPPER = 1.148
# Pressure Between + Invert（BetweenThreshold；不勾 Invert 时区间内单元过多，几乎看不出变化）
_PRESSURE_THRESHOLD_LOWER = 98660.0
_PRESSURE_THRESHOLD_UPPER = 104000.0
# Density + Invert
_INVERT_THRESHOLD_LOWER = 0.252
_INVERT_THRESHOLD_UPPER = 1.189

def DefaultThreshold():
    """Threshold：Density + Between，Apply 后 Fit 并截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.threshold_panel", 0, 8)
    ui.wait_alias("post.threshold.combo_scalars", 30.0)
    ui.combo_click("post.threshold.combo_scalars", "Density")
    ui.item_input_value("post.threshold.lower", _THRESHOLD_LOWER)
    ui.item_input_value("post.threshold.upper", _THRESHOLD_UPPER)
    ui.item_click_apply("post.threshold.apply", 0, 8)
    ui.wait_alias("post.ribbon.mesh_threshold1", 30.0)
    if ui.item_is_checked("post.ribbon.vis_vol19"):
        ui.item_click("post.ribbon.vis_vol19", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)


def BetweenThreshold():
    """Threshold：Pressure + Between [98660, 104000] + Invert，Apply 后 Fit 并截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.threshold_panel", 0, 8)
    ui.wait_alias("post.threshold.combo_scalars", 30.0)
    ui.combo_click("post.threshold.combo_scalars", "Pressure")
    ui.item_input_value("post.threshold.lower", _PRESSURE_THRESHOLD_LOWER)
    ui.item_input_value("post.threshold.upper", _PRESSURE_THRESHOLD_UPPER)
    ui.scroll_to_bottom("post.threshold.plugin_window")
    ui.wait_alias("post.threshold.invert")
    ui.item_click("post.threshold.invert", 0, 8)
    ui.item_click_apply("post.threshold.apply", 0, 8)
    ui.wait_alias("post.ribbon.mesh_threshold1", 30.0)
    if ui.item_is_checked("post.ribbon.vis_vol19"):
        ui.item_click("post.ribbon.vis_vol19", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)


def BelowLowerThreshold():
    """Threshold：Density + Below Lower Threshold。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.threshold_panel", 0, 8)
    ui.wait_alias("post.threshold.combo_scalars", 30.0)
    ui.combo_click("post.threshold.combo_scalars", "Density")
    ui.combo_click("post.threshold.combo_method", "Below Lower Threshold")
    ui.item_input_value("post.threshold.lower", _THRESHOLD_LOWER)
    ui.item_click_apply("post.threshold.apply", 0, 8)
    ui.wait_alias("post.ribbon.mesh_threshold1", 30.0)
    if ui.item_is_checked("post.ribbon.vis_vol19"):
        ui.item_click("post.ribbon.vis_vol19", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)


def InvertThreshold():
    """Threshold：Density + Between [0.252, 1.189] + Invert，Apply 后 Fit 并截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.threshold_panel", 0, 8)
    ui.wait_alias("post.threshold.combo_scalars", 30.0)
    ui.combo_click("post.threshold.combo_scalars", "Density")
    ui.item_input_value("post.threshold.lower", _INVERT_THRESHOLD_LOWER)
    ui.item_input_value("post.threshold.upper", _INVERT_THRESHOLD_UPPER)
    ui.scroll_to_bottom("post.threshold.plugin_window")
    ui.wait_alias("post.threshold.invert")
    ui.item_click("post.threshold.invert", 0, 8)
    ui.item_click_apply("post.threshold.apply", 0, 8)
    ui.wait_alias("post.ribbon.mesh_threshold1", 30.0)
    if ui.item_is_checked("post.ribbon.vis_vol19"):
        ui.item_click("post.ribbon.vis_vol19", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)


