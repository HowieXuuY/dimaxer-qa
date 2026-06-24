import dimaxer_ui as ui

# Bug: https://project.feishu.cn/dimaxer-dev/issue/detail/6698945943


def p0_insitu_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.insitu_panel", 0, 8)
    ui.item_click("post.insitu.exit", 0, 8)
