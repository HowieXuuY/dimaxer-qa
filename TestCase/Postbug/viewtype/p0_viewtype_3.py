import imgui_test_engine as te

import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6616780866


def p0_viewtype_3():
    ui.item_click_ref("//##vtkRenderWindow/VerticalTabs/\uf067", 0, 8)
    ui.item_click_ref("//##Popup_cec68140/Render View", 0, 8)

    ui.item_click("post.vtk_render_window.view_type", 0, 8)
    ui.item_click_ref("//##Popup_a35da901/Plot View", 0, 8)
    ui.item_click("post.quickaccess.xy_plot", 0, 8)
    ui.item_click("post.line_chart_view1.close", 0, 8)
    ui.item_click("post.xyplot.plugin_close", 0, 8)
    te.Yield(2)
    ui.tab_close("post.vtk_render_window.vertical_tabs_scene2_tab")
