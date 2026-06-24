import imgui_test_engine as te
import dimaxer_ui as ui
# https://project.feishu.cn/dimaxer-dev/issue/detail/7013509495?parentUrl=%2Fdimaxer-dev%2Fissue%2Fhomepage
def crash():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()
    ui.item_click("post.quickaccess.show_by_volume")
    ui.item_click("post.ribbonscene.meshes.visibility_checkbox_volume")
    ui.item_click("post.ribbonscene.scene_properties.table_button")
    ui.item_click("post.popup.colormap_editor.table_button")