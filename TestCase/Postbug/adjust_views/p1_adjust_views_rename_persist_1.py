import dimaxer_ui as ui

_RENAMED = "QA_ViewPoint_Renamed"


def p1_adjust_views_rename_persist_1():
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.adjust_views_panel", 0, 8)
    ui.wait_alias("post.adjust_views.add")

    ui.item_click("post.adjust_views.add", 0, 8)
    ui.wait_ui_idle()
    ui.wait_alias("post.adjust_views.name_1")

    ui.item_double_click("post.adjust_views.name_1", 8)
    ui.item_input_value("post.adjust_views.name_1", _RENAMED)
    ui.wait_ui_idle()

    ui.item_click("post.top.adjust_views_panel", 0, 8)
    ui.wait_ui_idle()

    ui.item_click("post.top.adjust_views_panel", 0, 8)
    ui.wait_alias("post.adjust_views.name_1")

    text = ui.item_read_string("post.adjust_views.name_1").strip()
    if text != _RENAMED:
        raise RuntimeError(
            f"post.adjust_views.name_1 expected {_RENAMED!r}, got {text!r}"
        )

    ui.item_click("post.adjust_views.clear_all", 0, 8)
    ui.wait_ui_idle()

    ui.item_click("post.top.adjust_views_panel", 0, 8)
