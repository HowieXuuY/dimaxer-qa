import dimaxer_ui as ui
# https://project.feishu.cn/dimaxer-dev/issue/detail/6793570496

_CHECKS = (
    "post.rom.add_var.check_0",
    "post.rom.add_var.check_1",
    "post.rom.add_var.check_2",
    "post.rom.add_var.check_3",
)


def p1_rom_add_variable_exit_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.rom_panel", 0, 8)
    ui.item_click("post.rom.add_variable")
    for alias in _CHECKS:
        ui.item_click(alias)
    ui.item_click("post.rom.add_var.exit")

    ui.item_click("post.rom.add_variable")
    for alias in _CHECKS:
        if ui.item_is_checked(alias):
            raise RuntimeError(f"{alias} should be unchecked after Exit and reopen")
