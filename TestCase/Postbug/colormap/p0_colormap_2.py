import imgui_test_engine as te

import dimaxer_ui as ui

# https://project.feishu.cn/dimaxer-dev/issue/detail/6686841885


def p0_colormap_2():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    # 选中 vol
    ui.item_click("post.ribbon.mesh_select_19")

    # 打开场景属性并选择 Density
    ui.item_click("post.scene_properties.value_cell", 0, 8)
    ui.item_click("post.scene_properties.density", 0, 8)
    
    ui.item_click("post.scene_properties.editor_launch")

    # 打开颜色映射编辑器
    ui.item_click("post.colormap.editor_table_button", 0, 8)

    # 打开后直接点场景树该项
    ui.item_click("post.scene_tree.select_bcid_12", 0, 8)
