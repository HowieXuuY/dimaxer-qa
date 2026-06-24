import imgui_test_engine as te

import dimaxer_ui as ui


def p0_viewtype_5():
    """Plot View + Measurement, then Link Camera (blocked), close Measurement and PlotView1."""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")

    # Step 01: Open Plot View (view-type tab → Plot View popup item)
    ui.item_click("post.vtk_render_window.view_type", 0, 8)
    ui.item_click("post.view_type.plot_view", 0, 8)

    # Step 02: Open Measurement（新开 Plot View 后焦点在折线图，须先切回 RenderView）
    ui.item_click("post.vtk_render_window.vertical_tabs_scene1_tab", 0, 8)
    ui.item_click("post.renderview1", 0, 8)
    ui.wait_ui_idle()
    ui.item_click("post.quickaccess.measurement", 0, 8)
    ui.wait_alias("post.measurement.plugin_close")

    # Step 03: Link Camera while Measurement is open (expected UI block / overlap)
    ui.item_click("post.quickaccess.link_camera", 0, 8)

    # Step 04: Close Measurement panel
    ui.item_click("post.measurement.plugin_close", 0, 8)

    # Step 05: Close Plot View 1 (line chart tab)
    ui.item_click("post.line_chart_view1.close", 0, 8)
