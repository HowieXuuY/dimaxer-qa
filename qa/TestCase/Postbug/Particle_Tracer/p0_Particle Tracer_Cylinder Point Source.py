import imgui_test_engine as te
import dimaxer_ui as ui
# https://project.feishu.cn/k112k5/issue/detail/7015679617?parentUrl=%2Fk112k5%2Fissue%2Fhomepage

def particle_tracer_cylinder_point_source():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.select_view_ribbon_tab()
    ui.item_click("view.camera.isometric_view")
    ui.select_post_ribbon_tab()
    ui.item_click("post.ribbon.vis_vki59")
    ui.item_click("post.top.particle_tracer_panel")
    ui.combo_click("post.particle_tracer.seeds", "CylinderPointSource")
    ui.item_click("post.particle_tracer.show_cylinder")
    ui.capture_renderview(8)