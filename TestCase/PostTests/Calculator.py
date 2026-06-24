import imgui_test_engine as te

import dimaxer_ui as ui


def CurlCalculator():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.calculator_panel")
    ui.item_click("post.calculator.add_btn")
    ui.item_click_apply("post.calculator.apply")
    ui.item_click("post.ribbon.mesh_calc_result")
    ui.combo_click("post.ribbon.scene_result_combo", "Result")
    te.Sleep(1)
    ui.capture_renderview(8)
