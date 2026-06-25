import imgui_test_engine as te
import dimaxer_ui as ui
# https://project.feishu.cn/k112k5/issue/detail/7015642590?parentUrl=%2Fk112k5%2Fissue%2Fhomepage

def particle_tracer_high_res_line_source():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.ribbon.vis_vki59")
    ui.item_click("post.top.particle_tracer_panel")
    ui.combo_click("post.particle_tracer.seeds", "HighResLineSource")
    ui.item_click("post.particle_tracer.show_line")
    ui.item_click("post.ribbon.hide_all")
    ui.item_click("post.ribbon.vis_particle_tracer1")

    ui.capture_renderview(8)
