import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6610891294


def p0_contour_2():
    """Contour：打开面板后 ImportFile，+ → Apply → QuickAccess「Show By Fluid」。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.contour_panel", 0, 8)
    ui.combo_click("post.contour.combo_multi_mode", "ImportFile")
    ui.item_click("post.contour.roweditor_plus")
    ui.item_click_apply("post.contour.apply", 0, 8)
    ui.item_click("post.quickaccess.show_by_fluid", 0, 8)
