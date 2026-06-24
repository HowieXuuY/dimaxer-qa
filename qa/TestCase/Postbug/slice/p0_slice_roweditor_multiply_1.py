import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6612695354


def p0_slice_roweditor_multiply_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.slice_panel", 0, 8)

    ui.item_click("post.slice.roweditor_plus")
    ui.item_click("post.slice.roweditor_plus")
    ui.item_input_value("post.slice.roweditor_edit_r2", 0.25)
    ui.item_click("post.slice.roweditor_x")
    ui.item_click("post.slice.roweditor_plus")
    ui.item_click("post.slice.exit")
