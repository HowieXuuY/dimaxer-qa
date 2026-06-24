import dimaxer_ui as ui

_MODEL = r"dmh1/19-0.000949999958.dmh.dat"


def Hub_To_Shroud():
    """Hub To Shroud 全功能测试：一次导入，依次覆盖所有参数组合。"""

    # ── 初始化 ──────────────────────────────────────────────
    ui.import_model_post(_MODEL)
    ui.ribbon_hide_all_and_select_mesh()
    ui.capture_renderview(8)

    # ── 1. 默认参数 Apply ───────────────────────────────────
    ui.item_click("post.top.hub_to_shroud_panel", 0, 8)
    ui.item_click_apply("post.hub_to_shroud.apply", 0, 8)
    ui.capture_renderview(8)

    # ── 2. Scalars: Pressure ────────────────────────────────
    ui.item_click("post.top.hub_to_shroud_panel", 0, 8)
    ui.combo_click("post.hub_to_shroud.scalars", "Pressure")
    ui.item_click_apply("post.hub_to_shroud.apply", 0, 8)
    ui.capture_renderview(8)

    # ── 3. Scalars: Wall Distance + Streamwise 0.5 ──────────
    ui.item_click("post.top.hub_to_shroud_panel", 0, 8)
    ui.combo_click("post.hub_to_shroud.scalars", "Wall Distance")
    ui.item_input_value("post.hub_to_shroud.streamwise", 0.5)
    ui.item_click_apply("post.hub_to_shroud.apply", 0, 8)
    ui.capture_renderview(8)

    # ── 4. Wall Distance + Streamwise 0.5 + Span Samples 150
    ui.item_click("post.top.hub_to_shroud_panel", 0, 8)
    ui.combo_click("post.hub_to_shroud.scalars", "Wall Distance")
    ui.item_input_value("post.hub_to_shroud.streamwise", 0.5)
    ui.item_input_value("post.hub_to_shroud.span_samples", 150)
    ui.item_click_apply("post.hub_to_shroud.apply", 0, 8)
    ui.capture_renderview(8)

    # ── 5. Wall Distance + Streamwise 1 + Span Samples 1500 + Circ Average: Mass
    ui.item_click("post.top.hub_to_shroud_panel", 0, 8)
    ui.combo_click("post.hub_to_shroud.scalars", "Wall Distance")
    ui.item_input_value("post.hub_to_shroud.streamwise", 1)
    ui.item_input_value("post.hub_to_shroud.span_samples", 1500)
    ui.combo_click("post.hub_to_shroud.circ_average", "Mass")
    ui.item_click_apply("post.hub_to_shroud.apply", 0, 8)
    ui.capture_renderview(8)

    # ── 6. Color Map: Pressure → Play ───────────────────────
    ui.combo_click("post.scene_properties.value_cell", "Pressure")
    ui.item_click("post.quickaccess.play", 0, 8)
    ui.capture_renderview(8)
