import os

import imgui_test_engine as te

import dimaxer_ui as ui


def NumberContour():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.contour_panel")
    ui.combo_click("post.contour.combo_quantity", "Pressure")
    ui.item_input_value("post.contour.input_generate_number", 3)
    ui.item_click_apply("post.contour.apply")
    ui.item_click("post.quickaccess.fit_data")
    te.Sleep(1)
    ui.capture_renderview(8)


def ImportFileContour():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.contour_panel")
    ui.combo_click("post.contour.combo_multi_mode", "ImportFile")
    ui.item_click("post.contour.import_datasource")
    filePath = os.path.join(te.GetWorkSpacePath(), "Model", "ContourValues.csv")
    ui.item_input_value("post.dialog.open_file_input", filePath)
    ui.item_click_apply("post.contour.apply")
    ui.item_click("post.quickaccess.fit_data")
    te.Sleep(1)
    ui.capture_renderview(8)
