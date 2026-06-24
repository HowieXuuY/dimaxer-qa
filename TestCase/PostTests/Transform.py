import imgui_test_engine as te

import dimaxer_ui as ui

# PostTests：Transform 功能回归（默认 dmh vol 19，截图比对渲染视图）。
# Transform 下拉为 proxy 名：Transform / RotateAroundOriginTransform / Reflect。


def DefaultTransform():
    """Transform：默认 Transform 类型，平移 + 绕 Z 旋转，Apply 后 Fit 并截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.transform_panel", 0, 8)
    ui.item_input_value("post.transform.translate_0", 0.05)
    ui.item_input_value("post.transform.rotate_2", 30.0)
    ui.item_click_apply("post.transform.apply", 0, 8)
    ui.wait_alias("post.ribbon.mesh_pvtransform1", 30.0)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)


def ScaledTransform():
    """Transform：Transform 类型 + 非均匀 Scale，Apply 后 Fit 并截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.transform_panel", 0, 8)
    ui.item_input_value("post.transform.scale_0", 1.2)
    ui.item_input_value("post.transform.scale_1", 0.8)
    ui.item_input_value("post.transform.scale_2", 1.0)
    ui.item_click_apply("post.transform.apply", 0, 8)
    ui.wait_alias("post.ribbon.mesh_pvtransform1", 30.0)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)


def RotateAroundOriginTransform():
    """Transform：RotateAroundOriginTransform，设置 Origin + Rotate 后 Apply 并截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.transform_panel", 0, 8)
    ui.combo_click("post.transform.combo_type", "RotateAroundOriginTransform")
    ui.item_input_value("post.transform.origin_0", 0.0)
    ui.item_input_value("post.transform.origin_1", 0.0)
    ui.item_input_value("post.transform.origin_2", 0.0)
    ui.item_input_value("post.transform.rotate_2", 45.0)
    ui.item_click_apply("post.transform.apply", 0, 8)
    ui.wait_alias("post.ribbon.mesh_pvtransform1", 30.0)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)


def ReflectTransform():
    """Transform：Reflect + Plane=X + Center 偏移，Apply 后 Fit 并截图。"""
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.transform_panel", 0, 8)
    ui.combo_click("post.transform.combo_type", "Reflect")
    ui.wait_alias("post.transform.combo_plane")
    ui.combo_click("post.transform.combo_plane", "X")
    # Center=0 时 vol 19 近似关于 x=0 对称，Copy Input 并集与原模型重叠，截图几乎无变化。
    ui.item_input_value("post.transform.center_0", 0.25)
    ui.item_click_apply("post.transform.apply", 0, 8)
    ui.wait_alias("post.ribbon.mesh_pvtransform1", 30.0)
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    te.Sleep(1)
    ui.capture_renderview(8)
