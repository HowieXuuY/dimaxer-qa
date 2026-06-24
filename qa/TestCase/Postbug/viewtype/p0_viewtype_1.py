import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6469244507
# 无 import_model_post：复现依赖协作台/前置用例已打开的 Post 会话。


def p0_viewtype_1():
    ui.item_click("post.vtk_render_window.view_type", 0, 8)
    ui.item_click("post.view_type.render_view", 0, 8)
    ui.item_click("post.quickaccess.link_camera", 0, 8)
    ui.item_click("post.link_camera.link", 0, 8)
    ui.item_click("post.link_camera.exit", 0, 8)
    ui.item_click("post.vtk_render_window.vertical_tabs_close", 0, 8)
