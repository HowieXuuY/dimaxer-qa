import dimaxer_ui as ui

#https://project.feishu.cn/k112k5/issue/detail/7020035676?parentUrl=%2Fk112k5%2Fissue%2Fhomepage&openScene=2

def p0_times_integration_1():

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

    # 4. 展开时间工具条
    if not ui.alias_exists_now("post.quickaccess.forward_step"):
        ui.item_click("post.quickaccess.toolbar_expand", 0, 8)
        ui.wait_ui_idle()

    # 5. 时间点下拉框：逐个选择 0.00000000 ~ 0.00029999
    time_points = [
        "0.00000000",
        "0.00009999",
        "0.00019999",
        "0.00029999",
    ]
    for tp in time_points:
        ui.combo_click("post.quickaccess.animation_combo", tp)
        ui.wait_ui_idle()

    # 6. Index 输入框：依次输入 0 ~ 3
    for i in range(4):
        ui.item_input_value("post.quickaccess.animation_index", i)
        ui.wait_ui_idle()

    # 7. Index +1 / -1 按键
    for _ in range(3):
        ui.item_click("post.quickaccess.animation_index_up", 0, 8)
        ui.wait_ui_idle()
    for _ in range(3):
        ui.item_click("post.quickaccess.animation_index_down", 0, 8)
        ui.wait_ui_idle()

    # 8. 前进 / 后退 步进
    for _ in range(2):
        ui.item_click("post.quickaccess.forward_step", 0, 8)
        ui.wait_ui_idle()
    for _ in range(2):
        ui.item_click("post.quickaccess.backward_step", 0, 8)
        ui.wait_ui_idle()

    # 9. 快进到最后 / 快退到第一步
    ui.item_click("post.quickaccess.step_to_end", 0, 8)
    ui.wait_ui_idle()
    ui.item_click("post.quickaccess.step_to_begin", 0, 8)
    ui.wait_ui_idle()

    ui.item_click("post.quickaccess.play", 0, 8)

    ui.capture_renderview(8)
