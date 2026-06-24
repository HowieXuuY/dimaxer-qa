import dimaxer_ui as ui

# https://project.feishu.cn/dimaxer-dev/issue/detail/6793570496
_EXPECT_MSG = "Please select valid source from model tree!"


def p1_slice_source_missing_after_delete_1():
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")

    ui.item_click("post.ribbon.mesh_select_assembly_19", 0, 8)
    ui.item_click("post.ribbon.mesh_select_assembly_19", 1)
    ui.item_click("post.scene_tree.popup_delete", 0, 8)
    ui.wait_ui_idle()

    ui.item_click("post.top.slice_panel", 0, 8)
    ui.wait_alias("post.slice.source_text")

    text = ui.item_read_string("post.slice.source_text").strip()
    if text != _EXPECT_MSG:
        raise RuntimeError(f"Slice Source expected {_EXPECT_MSG!r}, got {text!r}")
