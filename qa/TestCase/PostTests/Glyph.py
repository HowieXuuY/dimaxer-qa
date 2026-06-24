import imgui_test_engine as te

import dimaxer_ui as ui

# PostTests：Glyph 过滤器功能回归（默认 dmh vol 19，截图比对渲染视图）。
# Advanced Options 展开状态会跨用例保留：需要 Advanced 的用例开头点开展开、末尾再点一次合上。


def ArrowGlyph():
    """Glyph：默认 Arrow 源，Apply 后 Fit 并截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.glyph_panel", 0, 8)
    ui.item_click_apply("post.glyph.apply", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)


def ConeGlyph():
    """Glyph：Cone 源类型，Apply 后截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.glyph_panel", 0, 8)
    ui.item_click("post.glyph.combo_glyph_type", 0, 8)
    ui.item_click("post.glyph.combo_glyph_type_conesource", 0, 8)
    ui.item_click_apply("post.glyph.apply", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)


def ScaledArrowGlyph():
    """Glyph：Arrow + Tip Length + ScaleFactor。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.glyph_panel", 0, 8)
    # Source Setting：Tip Length（无需 Advanced）
    ui.item_click("post.glyph.tip_length", 0, 8)
    ui.item_input_value("post.glyph.tip_length", 0.35)
    # 展开 Advanced Options → ScaleFactor
    ui.item_click("post.glyph.advanced_options", 0, 8)
    ui.item_click("post.glyph.scale_factor", 0, 8)
    ui.item_input_value("post.glyph.scale_factor", 2.0)

    ui.item_click_apply("post.glyph.apply", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)
    ui.item_click("post.top.glyph_panel", 0, 8)
    ui.item_click("post.glyph.advanced_options", 0, 8)


def AllPointsConeGlyph():
    """Glyph：Cone + Glyph Mode = All Points。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.glyph_panel", 0, 8)
    ui.item_click("post.glyph.combo_glyph_type", 0, 8)
    ui.item_click("post.glyph.combo_glyph_type_conesource", 0, 8)
    ui.item_click("post.glyph.advanced_options", 0, 8)
    ui.combo_click("post.glyph.combo_glyph_mode", "All Points")
    ui.item_click_apply("post.glyph.apply", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)
    ui.item_click("post.top.glyph_panel", 0, 8)
    ui.item_click("post.glyph.advanced_options", 0, 8)
