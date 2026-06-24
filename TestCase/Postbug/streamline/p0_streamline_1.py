import imgui_test_engine as te

import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6604166714


def p0_streamline_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.stream_line_panel", 0, 8)
    ui.item_click_apply("post.stream_line.apply", 0, 8)

    ui.item_click("post.ribbon.mesh_streamtracer1", 0, 8)

    ui.item_click("post.top.stream_line_panel", 0, 8)
    ui.item_click_apply("post.stream_line.apply", 0, 8)

    ui.item_click("post.top.stream_line_panel", 0, 8)

    ui.item_click("post.stream_line.combo_vectors", 0, 8)
    ui.item_click("post.stream_line.combo_vectors_velocity_item", 0, 8)
    ui.item_click_apply("post.stream_line.apply", 0, 8)
