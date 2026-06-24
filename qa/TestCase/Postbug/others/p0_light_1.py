import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6689683945


def p0_light_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.scene.main_tabs.lighting", 0, 8)

    for _ in range(3):
        ui.item_click("post.scene.lighting.add", 0, 8)

    for _ in range(4):
        ui.item_click("post.scene.lighting.remove", 0, 8)

    ui.item_click("post.scene.lighting.light_edit", 0, 8)
    ui.item_click("post.scene.main_tabs.properties", 0, 8)
