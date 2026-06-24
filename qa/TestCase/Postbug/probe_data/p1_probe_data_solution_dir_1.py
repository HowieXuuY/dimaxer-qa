import os

import imgui_test_engine as te
import dimaxer_ui as ui


def p1_probe_data_solution_dir_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.probe_data_generation_panel", 0, 8)
    ui.item_click("post.probe_data.solution_dir_browse")
    ui.item_input_value(
        "post.dialog.open_file_input",
        os.path.join(te.GetWorkSpacePath(), "Model", "dmh1"),
    )

    if not ui.item_read_string("post.probe_data.solution_text").strip():
        raise RuntimeError("Solution Dir empty after selecting dmh1")

    ui.item_click("post.probe_data.exit")

    ui.item_click("post.top.probe_data_generation_panel", 0, 8)
    if ui.item_read_string("post.probe_data.solution_text").strip():
        raise RuntimeError("Solution Dir not cleared after Exit and reopen")
