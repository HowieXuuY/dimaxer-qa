
# bug 链接
# https://project.feishu.cn/dimaxer-dev/issue/detail/6594030914
# 无 import_model_post：复现 QuickAccess 双击行为，依赖已打开的 Post 会话。

import dimaxer_ui as ui


def p0_quickaccess_1():
    ui.item_click("post.quickaccess.fit_data", 0, 8)
    ui.item_click("post.quickaccess.fit_data", 0, 8)

    ui.item_click("post.quickaccess.rotation", 0, 8)
    ui.item_click("post.quickaccess.rotation", 0, 8)

    ui.item_click("post.quickaccess.link_camera", 0, 8)
    ui.item_click("post.quickaccess.link_camera", 0, 8)
