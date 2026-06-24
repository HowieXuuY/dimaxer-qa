import imgui_test_engine as te

import dimaxer_ui as ui


def p0_colormap_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")

    # 选中 vol
    ui.item_click("post.ribbon.mesh_select_19")

    # 打开场景属性并选择 Density
    ui.item_click("post.scene_properties.value_cell", 0, 8)
    ui.item_click("post.scene_properties.density", 0, 8)
    ui.item_click("post.scene_properties.editor_launch")

    # 打开颜色映射编辑器相关按钮
    ui.item_click("post.colormap.editor_table_button", 0, 8)
    ui.item_click("post.colormap.advanced_collapse", 0, 8)
    # 最后点击 Slice
    ui.item_click("post.top.slice_panel", 0, 8)
    ui.item_click("post.slice.exit", 0, 8)
