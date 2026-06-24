import imgui_test_engine as te

import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6980746399
def p0_viewtype_4():
    ui.item_click("post.vtk_render_window.view_type", 0, 8)
    ui.item_click("post.view_type.plot_view", 0, 8)
    ui.item_click("post.top.adjust_views_panel", 0, 8)
    ui.item_click("post.adjust_views.plugin_close", 0, 8)
    ui.item_click("post.line_chart_view1.close", 0, 8)
