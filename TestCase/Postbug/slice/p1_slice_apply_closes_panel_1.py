import dimaxer_ui as ui

# C++: ImgPopupBase::apply → dialogIsOpen_=false（NeedOpenWhenApply 默认 false）


def p1_slice_apply_closes_panel_1():
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.slice_panel", 0, 8)
    ui.wait_alias("post.slice.apply")

    ui.item_click_apply("post.slice.apply", 0, 8)
    ui.wait_ui_idle()

    if ui.alias_exists_now("post.slice.apply"):
        raise RuntimeError("post.slice.apply still visible after Apply; panel should close")
