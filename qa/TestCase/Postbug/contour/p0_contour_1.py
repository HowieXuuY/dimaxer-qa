import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6612443244


def p0_contour_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.contour_panel", 0, 8)

    ui.item_click("post.contour.roweditor_plus")
    ui.item_input_value("post.contour.roweditor_edit_r1", 2)

    ui.item_click("post.contour.combo_multi_mode")
    ui.item_click("post.contour.combo_import_file_item")
    ui.item_click("post.contour.roweditor_plus")
    ui.item_click_apply("post.contour.apply", 0, 8)
