
import dimaxer_ui as ui

_MODEL = r"dmh1/19-0.000949999958.dmh.dat"


def Reports():
    """Reports 全功能测试：一次导入，依次覆盖默认 Apply、Average+Temperature、Scene2 可视化。"""

    # ── 初始化 ──────────────────────────────────────────────
    ui.import_model_post(_MODEL)
    ui.ribbon_hide_all_and_select_mesh()
    ui.capture_renderview(8)

    # ── 1. 默认参数 Apply ───────────────────────────────────
    ui.item_click("post.top.reports_panel", 0, 8)
    ui.item_click_apply("post.reports.apply", 0, 8)
    ui.capture_renderview(8)

    # ── 2. Option: Average + Field Variable: Temperature ────
    ui.item_click("post.top.reports_panel", 0, 8)
    ui.combo_click("post.reports.option_combo", "Average")
    ui.combo_click("post.reports.field_variable_combo", "Temperature")
    ui.item_click_apply("post.reports.apply", 0, 8)
    ui.capture_renderview(8)

    # ── 3. Reports → Scene2 (SpreadSheet View) → 可见性 ────
    ui.item_click("post.top.reports_panel", 0, 8)
    ui.item_click_apply("post.reports.apply", 0, 8)

    if not ui.alias_exists_now("post.vtk_render_window.vertical_tabs_scene2_tab"):
        ui.item_click("post.vtk_render_window.vertical_tabs_add_scene", 0, 8)
        ui.item_click("post.view_type.spreadsheet_view", 0, 8)

    ui.item_click("post.vtk_render_window.vertical_tabs_scene2_tab", 0, 8)
    ui.item_click("post.ribbon.vis_reports1", 0, 8)
    ui.capture_window("post.vtk_render_window", 8)

    # ── 回到 Scene1，关闭 Scene2 ────────────────────────────
    ui.item_click("post.vtk_render_window.vertical_tabs_scene1_tab", 0, 8)
    ui.tab_close("post.vtk_render_window.vertical_tabs_scene2_tab")
