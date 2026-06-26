import imgui_test_engine as te

import dimaxer_ui as ui
# https://project.feishu.cn/k112k5/issue/detail/7015435150?parentUrl=%2Fk112k5%2Fissue%2Fhomepage

def Multiplane():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.ribbonscene.meshes.visibility_checkbox_volume")
    ui.item_click("post.top.multislice_panel")
    ui.item_input_value("post.multislice.input_number", 10)
    ui.item_click("post.multiplane.show_preview")
    ui.item_click("post.multislice.input_offset")
    ui.item_input_value("post.multislice.input_offset", 0.1)
    ui.capture_renderview(8)
    ui.item_click("post.multislice.apply")
    ui.item_click("post.ribbon.hide_all")
    ui.item_click("post.ribbonscene.meshes.visibility_checkbox_volume")
    ui.select_view_ribbon_tab()
    ui.item_click("view.camera.isometric_view")
    ui.item_click("post.ribbon.vis_vol19")
    ui.item_click("post.scene_tree.vis_multiplane9")
    ui.capture_renderview(8)