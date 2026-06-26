import dimaxer_ui as ui

#https://project.feishu.cn/k112k5/issue/detail/7016048023?parentUrl=%2Fk112k5%2Fissue%2Fhomepage&openScene=2

def p0_color_style_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")

    # 选中 vol
    ui.item_click("post.ribbon.mesh_select_19")

    # Color Map 选 Pressure
    ui.combo_click("post.scene_properties.value_cell", "Pressure")

    # 点击 Auto Range
    ui.item_click("post.scene_properties.auto_range_btn", 0, 8)

    # 打开 Color Style 下拉框
    ui.item_click("post.scene_properties.color_style", 0, 8)

    # 下拉框滚到底，露出最底部的 Inferno (matplotlib)
    ui.scroll_to_bottom_ref("//##Combo_00")

    # 点击 Inferno (matplotlib)
    ui.item_click("post.scene_properties.color_style_inferno", 0, 8)
    ui.capture_renderview(8)

    # 打开 Color Style 下拉框，选 Viridis (matplotlib)
    ui.item_click("post.scene_properties.color_style", 0, 8)
    ui.scroll_to_bottom_ref("//##Combo_00")
    ui.item_click("post.scene_properties.color_style_viridis", 0, 8)
    ui.capture_renderview(8)
