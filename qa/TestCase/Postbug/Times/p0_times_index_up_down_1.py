import dimaxer_ui as ui

# https://project.feishu.cn/k112k5/issue/detail/7015460042?parentUrl=%2Fk112k5%2Fissue%2Fhomepage&openScene=2
def p0_times_index_up_down_1():
    """打开 vki_59_demo 模型 → 选中网格 → Color Map 选 Pressure → 展开工具条 → index +1 ×3 → index -1 ×3。"""

    dmx_path = r"/data2/cfd/hzh/qa/Model/vki_59_demo/simulations/vki_59_demo_simulation.dmx"

    # 1. 导入新模型
    ui.item_click("post.top.open_files", 0, 8)
    ui.item_input_value("post.dialog.open_file_input", dmx_path)
    ui.wait_alias("post.case_loader.apply")
    ui.item_click_apply("post.case_loader.apply", 0, 8)

    # 2. 选中 vki59 网格
    ui.item_click("post.ribbon.mesh_select_vki59", 0, 8)
    ui.wait_ui_idle()

    # 3. Color Map 选 Pressure
    ui.combo_click("post.scene_properties.value_cell", "Pressure")

    # 3.1 Value Range Min / Max
    ui.item_input_value("post.scene_properties.value_range_min", 1.013250e+05)
    ui.item_input_value("post.scene_properties.value_range_max", 1.013410e+05)

    # 4. 展开时间工具条（检测是否已展开）
    if not ui.alias_exists_now("post.quickaccess.forward_step"):
        ui.item_click("post.quickaccess.toolbar_expand", 0, 8)
        ui.wait_ui_idle()

    # 5. index +1 三次
    for _ in range(3):
        ui.item_click("post.quickaccess.animation_index_up", 0, 8)
        ui.wait_ui_idle()

    # 6. index -1 三次
    for _ in range(3):
        ui.item_click("post.quickaccess.animation_index_down", 0, 8)
        ui.wait_ui_idle()
    
    ui.capture_renderview(8)