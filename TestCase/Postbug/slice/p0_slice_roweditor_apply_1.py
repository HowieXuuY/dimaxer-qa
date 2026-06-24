import imgui_test_engine as te

import dimaxer_ui as ui
#bug 链接
#https://project.feishu.cn/dimaxer-dev/issue/detail/6622579712

def p0_slice_roweditor_apply_1():
    """Post 导入 → vol → Slice(Box) → 行编辑器 + → 改一项数值 → − → Apply。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.slice_panel", 0, 8)
    ui.combo_click("post.slice.combo_type", "Box")

    ui.item_click("post.slice.roweditor_plus")
    ui.item_input_value("post.slice.roweditor_edit_r1", 0.25)
    ui.item_click("post.slice.roweditor_minus")
    ui.item_click_apply("post.slice.apply", 0, 8)
