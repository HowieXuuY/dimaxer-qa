import imgui_test_engine as te

import dimaxer_ui as ui

# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6668185432
# ImGuiMod_Ctrl（imgui.h）用于 Ctrl+点击多选场景树
_IMGUI_MOD_CTRL = 4096

# 本用例右键菜单 Delete：##Popup 哈希随会话/菜单上下文变化，与其它 Delete 不同，保留 copy path。
_REF_SCENE_TREE_DELETE = r"//##Popup_5fc85139/Delete"


def p0_boundary_multi_delete_1():
    ui.import_model_post("dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    te.KeyDown(_IMGUI_MOD_CTRL)
    ui.item_click("post.scene_tree.select_bcid_11", 0, 8)
    te.KeyUp(_IMGUI_MOD_CTRL)

    te.KeyDown(_IMGUI_MOD_CTRL)
    ui.item_click("post.scene_tree.select_bcid_12", 0, 8)
    te.KeyUp(_IMGUI_MOD_CTRL)

    # 在多选上右键（点在 bcid_12 上）
    ui.item_click("post.scene_tree.select_bcid_12", 1, 8)

    ui.item_click_ref(_REF_SCENE_TREE_DELETE)
