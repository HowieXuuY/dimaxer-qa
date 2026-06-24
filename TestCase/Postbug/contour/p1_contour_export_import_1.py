import os

import imgui_test_engine as te

import dimaxer_ui as ui

_EXPECTED_VALUE = 1.5
_VALUE_EPS = 1e-4
_OUTPUT_DIR = "Output"
_CSV_NAME = "p1_contour_export_import_1.csv"
# https://project.feishu.cn/dimaxer-dev/issue/detail/6834805344

def p1_contour_export_import_1():
    """Contour：行编辑器 1.5 → 导出数据源 → 保存 CSV → ImportFile 再导入 → 校验仍为 1.5。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.contour_panel", 0, 8)
    ui.item_input_value("post.contour.roweditor_edit_r0", _EXPECTED_VALUE)

    csv_path = os.path.join(te.GetWorkSpacePath(), _OUTPUT_DIR, _CSV_NAME)
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    ui.item_click("post.contour.export_datasource")
    ui.wait_alias("post.dialog.save_file_input")
    # 须写完整路径（qa/Output/...）；只填文件名会落到 mod/cases/Untitled/
    ui.item_input_value("post.dialog.save_file_input", csv_path)
    ui.wait_ui_idle()

    ui.combo_click("post.contour.combo_multi_mode", "ImportFile")
    ui.item_click("post.contour.import_datasource")
    ui.wait_alias("post.dialog.open_file_input")
    ui.item_input_value("post.dialog.open_file_input", csv_path)
    ui.wait_ui_idle()
    ui.wait_alias("post.contour.roweditor_edit_r0", timeout_sec=30.0)

    actual = ui.item_read_float("post.contour.roweditor_edit_r0")
    if abs(actual - _EXPECTED_VALUE) > _VALUE_EPS:
        raise RuntimeError(
            f"Contour row editor expected {_EXPECTED_VALUE}, got {actual} (|delta| > {_VALUE_EPS})"
        )
