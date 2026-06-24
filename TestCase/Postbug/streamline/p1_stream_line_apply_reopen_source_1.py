import dimaxer_ui as ui

# C++: Apply 后 m_pEntity=nullptr 且关面板；再开应对新一次 InitTool，Source 仍指向有效 vol

_SOURCE_FAIL_MARKERS = (
    "Please select source from model tree",
    "Please select valid source from model tree",
)


def p1_stream_line_apply_reopen_source_1():
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")
    ui.ribbon_hide_all_and_select_mesh()

    ui.item_click("post.top.stream_line_panel", 0, 8)
    ui.wait_alias("post.stream_line.source_text")

    text = ui.item_read_string("post.stream_line.source_text").strip()
    for marker in _SOURCE_FAIL_MARKERS:
        if marker in text:
            raise RuntimeError(f"post.stream_line.source_text invalid before Apply: {text!r}")

    ui.item_click_apply("post.stream_line.apply", 0, 8)
    ui.wait_alias("post.ribbon.mesh_streamtracer1", timeout_sec=60.0)

    ui.item_click("post.top.stream_line_panel", 0, 8)
    ui.wait_alias("post.stream_line.source_text")

    text = ui.item_read_string("post.stream_line.source_text").strip()
    for marker in _SOURCE_FAIL_MARKERS:
        if marker in text:
            raise RuntimeError(
                f"post.stream_line.source_text invalid after Apply+reopen: {text!r}"
            )
