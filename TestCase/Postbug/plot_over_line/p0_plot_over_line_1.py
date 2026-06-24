import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6751420832


def p0_plot_over_line_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.plot_over_line_panel", 0, 8)
    ui.item_click("post.plot_over_line.apply", 0, 8)
    ui.item_click("post.scene_tree.select_plot_over_line1", 0, 8)
    ui.item_click("post.top.plot_over_line_panel", 0, 8)
    ui.item_click("post.plot_over_line.apply", 0, 8)
    ui.item_double_click("post.scene_tree.select_plot_over_line1", 8)
    ui.item_click("post.plot_over_line.reselect", 0, 8)
    ui.item_click("post.plot_over_line.apply", 0, 8)
    ui.item_click("post.scene_tree.select_plot_over_line2", 0, 8)
