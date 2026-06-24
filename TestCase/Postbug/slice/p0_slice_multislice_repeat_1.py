import imgui_test_engine as te

import dimaxer_ui as ui

#bug 链接
#https://project.feishu.cn/dimaxer-dev/issue/detail/6622531394
def p0_slice_multislice_repeat_1():
    """Post 导入 → 选中 vol → Slice 面板 Apply →（选中 Slice1 → MultiPlane → Apply）×3。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.slice_panel", 0, 8)
    ui.item_click_apply("post.slice.apply", 0, 8)

    for _ in range(3):
        ui.item_click("post.ribbon.mesh_slice1", 0, 8)
        ui.item_click("post.top.multislice_panel", 0, 8)
        ui.item_click_apply("post.multislice.apply", 0, 8)
