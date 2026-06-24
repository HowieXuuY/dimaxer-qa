import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6616780866


def p0_viewtype_2():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.vtk_render_window.view_type", 0, 8)
    ui.item_click("post.view_type.plot_view", 0, 8)
    ui.item_click("post.ribbon.vis_vol19", 0, 8)
    ui.item_click("post.vtk_render_window.view_type", 0, 8)
    ui.item_click("post.view_type.plot_view", 0, 8)
    ui.item_click("post.scene_tree.vis_bcid_11", 0, 8)
    ui.item_click("post.scene_tree.select_bcid_11", 0, 8)
    ui.item_click("post.quickaccess.xy_plot", 0, 8)
    ui.item_click("post.line_chart_view2.close", 0, 8)
    ui.item_click("post.line_chart_view1.close", 0, 8)
    ui.item_click("post.xyplot.plugin_close", 0, 8)
