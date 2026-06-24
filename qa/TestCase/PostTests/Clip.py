import imgui_test_engine as te

import dimaxer_ui as ui


def BoxClip():
    """Clip: box mode — applies box clip and captures the render view."""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.clip_panel", 0, 8)
    ui.combo_click("post.clip.combo_type", "Box")
    ui.item_click_apply("post.clip.apply")
    ui.capture_renderview(8)


def CylinderClip():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.clip_panel", 0, 8)
    ui.combo_click("post.clip.combo_type", "Cylinder")
    ui.item_click_apply("post.clip.apply")
    ui.capture_renderview(8)


def PlaneClip():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.clip_panel", 0, 8)
    ui.item_click_apply("post.clip.apply")
    ui.capture_renderview(8)


def ScalarClip():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.clip_panel", 0, 8)
    ui.combo_click("post.clip.combo_type", "Scalar")
    ui.item_click_apply("post.clip.apply")
    ui.capture_renderview(8)


def SphereClip():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.top.clip_panel", 0, 8)
    ui.combo_click("post.clip.combo_type", "Sphere")
    ui.item_click_apply("post.clip.apply")
    ui.capture_renderview(8)
