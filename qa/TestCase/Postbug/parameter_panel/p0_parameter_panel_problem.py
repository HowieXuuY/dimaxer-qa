import dimaxer_ui as ui


def parameter_panel_problem():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.slice_panel")
    ui.item_click("post.slice.apply")

    ui.item_click("post.top.slice_panel")
    ui.combo_click("post.slice.combo_type", "Box")
    ui.item_click("post.slice.apply")

    ui.item_double_click("post.ribbon.mesh_slice1")
    ui.capture_window("post.slice.plugin_window")
    ui.item_double_click("post.ribbon.mesh_slice2")
    ui.capture_window("post.slice.plugin_window")
