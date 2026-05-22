from pathlib import Path


FRONTEND = Path(__file__).resolve().parents[1] / "web" / "mask_iteration_app" / "index_merged.html"


def _html() -> str:
    return FRONTEND.read_text(encoding="utf-8")


def test_special_toolbar_only_exposes_required_quality_actions():
    html = _html()

    assert 'id="markWrongTargetBtn"' in html
    assert 'id="markDifficultBtn"' in html
    assert 'id="markBlurryImageBtn"' in html
    assert "标记错误框" in html
    assert "标记难处理" in html
    assert "删除模糊图" in html
    assert 'id="deleteTargetBtn"' not in html
    assert 'id="deleteImageBtn"' not in html
    assert "删除当前框" not in html
    assert "删除整张图" not in html


def test_run_copy_import_reads_real_folder_path_directly():
    html = _html()

    import_start = html.index("async function importRunCopyFolder()")
    import_end = html.index("async function openCurrentTarget", import_start)
    import_body = html[import_start:import_end]

    assert 'id="runCopyPathInput"' in html
    assert '"/api/import-run-copy-path"' in import_body
    assert "copy_root_path: copyRootPath" in import_body
    assert "importRunCopyFolderViaBatch" not in import_body
    assert "importRunCopyFolderViaServerChunks(selection)" not in import_body
    assert "runCopyFolderUpload" not in html


def test_prompt_record_hover_highlights_canvas_items():
    html = _html()

    assert "function wirePromptRecordHover" in html
    assert "data-hover-kind" in html
    assert "state.hoverPrompt" in html
    assert "function isHoveredPrompt" in html
    assert "drawPromptLabel" in html
