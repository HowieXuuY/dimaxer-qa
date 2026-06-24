import imgui_test_engine as te
import dimaxer_ui as ui
def NumberMultiSlice():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.multislice_panel")
    ui.item_input_value("post.multislice.input_number", 3)
    ui.item_input_value("post.multislice.input_offset", 0.3)
    ui.item_click_apply("post.multislice.apply")
    ui.item_click("post.quickaccess.fit_data")
    te.Sleep(1)
    ui.capture_renderview(8)
