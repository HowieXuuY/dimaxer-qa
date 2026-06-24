import dimaxer_ui as ui


def p1_monitor_name_input_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.monitor_panel", 0, 8)
    ui.item_input_value("post.monitor.name", "123")

    if ui.item_read_string("post.monitor.name").strip() != "123":
        raise RuntimeError("Monitor Name field expected '123'")
