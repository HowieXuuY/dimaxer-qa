import imgui_test_engine as te

import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6661362962

def p0_multiplane_1():
    """Post 导入 → vol → MultiPlane → Plane Mode 选 ImportPoints → Apply → 反复点击生成的 PostMultiPlane 场景行 15 次。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.multislice_panel", 0, 8)
    ui.combo_click("post.multislice.combo_plane_mode", "ImportPoints")

    # Wait Process Model progress before selecting scene row.
    ui.item_click_apply("post.multislice.apply", 0, 8)

    for _ in range(5):
        ui.item_click("post.scene_tree.select_multiplane1", 0, 8)
