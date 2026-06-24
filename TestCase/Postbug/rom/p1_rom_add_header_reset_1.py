import dimaxer_ui as ui

_HEADER_NAME = "123"

# https://project.feishu.cn/dimaxer-dev/issue/detail/6769402419
def p1_rom_add_header_reset_1():
    ui.item_click("post.top.rom_panel", 0, 8)
    ui.item_click("post.rom.add_header", 0, 8)
    ui.wait_alias("post.rom.header_name")

    ui.item_input_value("post.rom.header_name", _HEADER_NAME)
    ui.item_click("post.rom.header_apply", 0, 8)
    ui.wait_ui_idle()

    ui.item_click("post.rom.reset", 0, 8)
    ui.wait_ui_idle()

    ui.item_click("post.rom.add_header", 0, 8)
    ui.wait_alias("post.rom.header_name")

    text = ui.item_read_string("post.rom.header_name").strip()
    if text:
        raise RuntimeError(f"post.rom.header_name expected empty after Reset, got {text!r}")
