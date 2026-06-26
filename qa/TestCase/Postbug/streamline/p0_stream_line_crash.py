import dimaxer_ui as ui


def stream_line_crash():
    ui.select_post_ribbon_tab()
    ui.item_click("post.top.open_files")
    ui.item_input_value("post.dialog.open_file_input", "/data2/cfd/ccq/qa/Model/vki_59_demo/simulations/vki_59_demo_simulation.dmx")
    ui.wait_ui_idle()
    ui.item_click_apply("post.case_loader.apply")
    ui.item_click("post.ribbon.hide_all")
    ui.wait_ui_idle()
    ui.item_click("post.ribbon.mesh_select_vki59_1")
    ui.item_click("post.ribbon.vis_vki59_1")

    ui.item_click("post.top.stream_line_panel")
    ui.item_click("post.quickaccess.toolbar_expand")
    ui.item_click("post.quickaccess.forward")
    ui.item_click("post.quickaccess.forward")
    ui.item_click("post.quickaccess.forward")
    # ui.item_click("post.top.slice_panel")
    # ui.combo_click("post.slice.combo_type", "Box")
    # ui.item_click("post.slice.show_preview")
    # ui.item_input_value("post.slice.length", "0.05")
    # ui.item_click("post.slice.apply")

    # ui.item_click("post.ribbon.hide_all")
    # ui.item_click("post.ribbon.vis_slice1")
    ui.capture_renderview(8)
