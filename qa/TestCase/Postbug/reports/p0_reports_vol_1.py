import imgui_test_engine as te

import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6619755109


def p0_reports_vol_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.reports_panel", 0, 8)
    ui.item_click_apply("post.reports.apply", 0, 8)
