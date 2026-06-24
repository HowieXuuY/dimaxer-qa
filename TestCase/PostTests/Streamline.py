import imgui_test_engine as te

import dimaxer_ui as ui

# PostTests：Stream Line 功能回归（默认 dmh vol 19，截图比对渲染视图）。
# Advanced Options 展开后会出现第二组 Vectors（Integration Direction）；用例保持收起。


def DefaultStreamline():
    """Stream Line：默认 vol 19 源，Apply 后 Fit 并截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.stream_line_panel", 0, 8)
    ui.item_click_apply("post.stream_line.apply", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)


def SurfaceStreamline():
    """Stream Line：勾选 Surface Streamlines，Apply 后 Fit 并截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.stream_line_panel", 0, 8)
    ui.item_click("post.stream_line.surface_streamlines", 0, 8)
    ui.item_click_apply("post.stream_line.apply", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)


def SliceSourceStreamline():
    """Stream Line：先 Slice Apply，再以 Slice1 为源 Apply 并截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.slice_panel", 0, 8)
    ui.item_click_apply("post.slice.apply", 0, 8)
    ui.item_click("post.ribbon.mesh_slice1", 0, 8)

    ui.item_click("post.top.stream_line_panel", 0, 8)
    ui.item_click_apply("post.stream_line.apply", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)
