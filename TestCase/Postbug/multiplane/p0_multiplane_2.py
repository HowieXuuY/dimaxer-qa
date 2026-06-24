import imgui_test_engine as te

import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6660018171


def p0_multiplane_2():
    """Post 导入 → vol → MultiPlane → ImportPoints → Apply → 双击 Number 首行 → 输入 1001 → Apply。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.multislice_panel", 0, 8)
    ui.item_double_click_ref(
        r"//MultiPlane##CustomStatePlugin\/##MultiPlaneSettings_31FB93CD/Number/$$0/##v"
    )
    te.ItemInputValue(
        r"//MultiPlane##CustomStatePlugin\/##MultiPlaneSettings_31FB93CD/Number/$$0/##v",
        1001,
    )
    ui.item_click_apply("post.multislice.apply", 0, 8)
