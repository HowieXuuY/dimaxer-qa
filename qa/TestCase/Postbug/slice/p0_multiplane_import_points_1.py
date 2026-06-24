import imgui_test_engine as te

import dimaxer_ui as ui

#bug 链接
#https://project.feishu.cn/dimaxer-dev/issue/detail/6622580764
def p0_multiplane_import_points_1():
    """Post 导入 → 选中 vol → MultiPlane：Plane Mode 选 ImportPoints → +×3、-×4 → Apply。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.multislice_panel", 0, 8)

    ui.combo_click("post.multislice.combo_plane_mode", "ImportPoints")

    for _ in range(3):
        ui.item_click("post.multislice.picking_plus", 0, 8)
    for _ in range(4):
        ui.item_click("post.multislice.picking_minus", 0, 8)

    ui.item_click_apply("post.multislice.apply", 0, 8)
