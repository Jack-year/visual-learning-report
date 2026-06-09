#!/usr/bin/env python3
"""Generate Obsidian Canvas files for visual-learning-report.

Usage:
  python scripts/create_canvas.py visual model.json visual.canvas
  python scripts/create_canvas.py cards cards.json cards.canvas
  python scripts/create_canvas.py formulas formulas.json formulas.canvas

The script is intentionally small and deterministic so Claude Code can create
valid .canvas files without hand-writing coordinates every time.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

Color = Optional[str]

COLOR = {
    "core": "red",
    "problem": "red",
    "warning": "red",
    "trap": "red",
    "concept": "green",
    "mechanism": "green",
    "principle": "green",
    "formula": "blue",
    "math": "blue",
    "variable": "blue",
    "example": "yellow",
    "analogy": "yellow",
    "application": "yellow",
    "memory": "yellow",
    "risk": "purple",
    "limit": "purple",
    "ambiguity": "purple",
    "review": "gray",
    "source": "gray",
    "file": "gray",
}


def normalize_color(value: Any, fallback: str = "concept") -> Color:
    if value is None:
        return COLOR.get(fallback, fallback)
    key = str(value).strip().lower()
    return COLOR.get(key, key if key in {"red", "green", "blue", "yellow", "purple", "gray"} else COLOR.get(fallback, fallback))


def _text_node(
    node_id: str,
    text: str,
    x: int,
    y: int,
    width: int = 420,
    height: int = 240,
    color: Color = None,
) -> Dict[str, Any]:
    node: Dict[str, Any] = {
        "id": node_id,
        "type": "text",
        "text": text.strip() or "空节点",
        "x": x,
        "y": y,
        "width": width,
        "height": height,
    }
    if color:
        node["color"] = color
    return node


def _file_node(
    node_id: str,
    file_path: str,
    x: int,
    y: int,
    width: int = 360,
    height: int = 190,
    color: Color = "gray",
) -> Dict[str, Any]:
    node: Dict[str, Any] = {
        "id": node_id,
        "type": "file",
        "file": file_path,
        "x": x,
        "y": y,
        "width": width,
        "height": height,
    }
    if color:
        node["color"] = color
    return node


def _edge(edge_id: str, src: str, dst: str, label: str = "") -> Dict[str, Any]:
    out = {"id": edge_id, "fromNode": src, "toNode": dst}
    if label:
        out["label"] = label
    return out


def _bullets(items: Iterable[Any]) -> str:
    return "\n".join(f"- {item}" for item in items if str(item).strip())


def _format_value(value: Any) -> str:
    if value is None or value == "":
        return ""
    if isinstance(value, list):
        return " · ".join(str(v) for v in value if str(v).strip())
    return str(value)


def card_text(card: Dict[str, Any], card_type: str = "concept") -> str:
    if card_type == "formula":
        title = card.get("title") or card.get("name") or "未命名公式"
        original = card.get("original") or card.get("term") or ""
        latex = card.get("latex") or ""
        lines = [f"# 公式卡：{title}" + (f" / {original}" if original else "")]
        if latex:
            lines += ["", "$$", str(latex), "$$"]
        fields = [
            ("人话解释", card.get("plain")),
            ("变量解释", card.get("variables")),
            ("直觉图像", card.get("intuition")),
            ("工程/实践意义", card.get("meaning")),
            ("常见误解", card.get("misunderstanding")),
            ("来源位置", card.get("source")),
        ]
    else:
        title = card.get("title") or card.get("name") or "未命名概念"
        original = card.get("original") or card.get("term") or ""
        lines = [f"# 概念卡：{title}" + (f" / {original}" if original else "")]
        latex = card.get("latex") or card.get("formula")
        fields = [
            ("定义", card.get("definition")),
            ("公式", f"$$\n{latex}\n$$" if latex else None),
            ("直觉", card.get("intuition")),
            ("例子", card.get("example")),
            ("容易混淆", card.get("confusion")),
            ("相关概念", card.get("related")),
            ("置信度", card.get("confidence", "extracted")),
        ]
    for label, value in fields:
        value_text = _format_value(value)
        if not value_text:
            continue
        if value_text.startswith("$$"):
            lines += ["", f"## {label}", "", value_text]
        else:
            lines += ["", f"## {label}", value_text]
    return "\n".join(lines)


def card_dimensions(card: Dict[str, Any], formula: bool = False) -> tuple[int, int]:
    text_len = len(json.dumps(card, ensure_ascii=False))
    has_formula = bool(card.get("latex") or card.get("formula"))
    if formula or has_formula or text_len > 220:
        return int(card.get("width", 720)), int(card.get("height", 520))
    return int(card.get("width", 620)), int(card.get("height", 420))


def make_cards_canvas(model: Dict[str, Any], formula: bool = False) -> Dict[str, Any]:
    cards = model.get("formulas" if formula else "cards", [])
    if not cards and formula:
        cards = [{"title": "未提取到核心公式", "plain": "本材料没有可单独整理的核心公式。", "kind": "formula"}]
    title = model.get("title", "公式卡片" if formula else "概念卡片")
    nodes: List[Dict[str, Any]] = [
        _text_node(
            "title",
            f"# {title}\n\n{'公式卡片白板' if formula else '概念知识卡片白板'}",
            0,
            -300,
            680,
            200,
            normalize_color("formula" if formula else "concept"),
        )
    ]
    edges: List[Dict[str, Any]] = []
    cols = int(model.get("columns", 3)) or 3
    gap_x = int(model.get("gap_x", 120))
    gap_y = int(model.get("gap_y", 120))
    default_w = int(model.get("card_width", 720 if formula else 620))
    default_h = int(model.get("card_height", 520 if formula else 420))
    col_widths = [default_w for _ in range(cols)]
    row_heights: List[int] = []
    dimensions: List[tuple[int, int]] = []
    for idx, card in enumerate(cards):
        w, h = card_dimensions(card, formula=formula)
        dimensions.append((w, h))
        row, col = divmod(idx, cols)
        while len(row_heights) <= row:
            row_heights.append(default_h)
        col_widths[col] = max(col_widths[col], w)
        row_heights[row] = max(row_heights[row], h)
    total_w = sum(col_widths) + gap_x * (cols - 1)
    start_x = -total_w // 2
    y = 0
    for idx, card in enumerate(cards):
        row, col = divmod(idx, cols)
        x = start_x + sum(col_widths[:col]) + gap_x * col
        y = sum(row_heights[:row]) + gap_y * row
        w, h = dimensions[idx]
        node_id = f"{'formula' if formula else 'card'}-{idx+1}"
        color = normalize_color(card.get("color") or card.get("kind") or ("formula" if formula else "concept"), "formula" if formula else "concept")
        nodes.append(_text_node(node_id, card_text(card, "formula" if formula else "concept"), x, y, w, h, color))
        edges.append(_edge(f"edge-title-{node_id}", "title", node_id))
    return {"nodes": nodes, "edges": edges}


def section_text(section: Dict[str, Any]) -> str:
    title = section.get("title") or section.get("label") or "节点"
    text = section.get("text") or ""
    items = section.get("items") or []
    lines = [f"# {title}"]
    if text:
        lines += ["", str(text)]
    if items:
        lines += ["", _bullets(items)]
    return "\n".join(lines)


def make_visual_canvas(model: Dict[str, Any]) -> Dict[str, Any]:
    title = model.get("title", "Visual Learning Report")
    thesis = model.get("thesis", "可视化学习报告")
    nodes: List[Dict[str, Any]] = []
    edges: List[Dict[str, Any]] = []
    nodes.append(_text_node("center", f"# {title}\n\n{thesis}", 0, 0, 560, 260, normalize_color("concept")))

    defaults = [
        ("core-question", "核心问题", model.get("core_question", ""), "core", -640, -430),
        ("why", "为什么重要", model.get("why_it_matters", ""), "example", 0, -430),
        ("takeaway", "最终结论", model.get("takeaway", ""), "concept", 640, -430),
        ("background", "背景/上下文", model.get("background", ""), "review", -740, 0),
        ("limits", "局限/争议", model.get("limits", ""), "risk", 740, 0),
        ("examples", "例子/应用", model.get("examples", []), "example", -640, 450),
        ("review", "复习问题", model.get("review_questions", []), "review", 0, 450),
        ("memory", "记忆锚点", model.get("memory_anchors", []), "memory", 640, 450),
    ]
    for node_id, label, content, color, x, y in defaults:
        if isinstance(content, list):
            text = f"# {label}\n\n{_bullets(content)}"
        else:
            text = f"# {label}\n\n{content}".strip()
        nodes.append(_text_node(node_id, text, x, y, 460, 260, normalize_color(color)))
        edges.append(_edge(f"edge-center-{node_id}", "center", node_id))

    mechanisms = model.get("mechanisms", [])
    mech_y = 790
    mech_start_x = -690
    previous = "center"
    for idx, mech in enumerate(mechanisms[:4]):
        node_id = f"mechanism-{idx+1}"
        color = normalize_color(mech.get("color") or mech.get("kind") or "mechanism")
        nodes.append(_text_node(node_id, section_text(mech), mech_start_x + idx * 460, mech_y, 400, 250, color))
        edges.append(_edge(f"edge-{previous}-{node_id}", previous, node_id, "推导" if idx else "机制"))
        previous = node_id

    files = model.get("files", [
        {"path": "map.html", "label": "导览图"},
        {"path": "blackboard/01-core-question.html", "label": "黑板页 01"},
        {"path": "cards.canvas", "label": "概念卡片"},
        {"path": "formulas.canvas", "label": "公式卡片"},
        {"path": "ingest-ready.md", "label": "摄入材料"},
    ])
    file_y = 1130 if mechanisms else 790
    start_x = -900
    for idx, f in enumerate(files):
        file_id = f"file-{idx+1}"
        nodes.append(_file_node(file_id, f["path"], start_x + idx * 400, file_y, 340, 190, normalize_color("file")))
        edges.append(_edge(f"edge-center-{file_id}", "center", file_id, f.get("label", "文件")))

    for idx, edge in enumerate(model.get("edges", [])):
        edges.append(_edge(f"custom-edge-{idx+1}", edge["from"], edge["to"], edge.get("label", "")))

    return {"nodes": nodes, "edges": edges}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Obsidian Canvas JSON files.")
    parser.add_argument("mode", choices=["visual", "cards", "formulas"], help="Canvas type to create")
    parser.add_argument("input_json", help="Path to model JSON")
    parser.add_argument("output_canvas", help="Path to output .canvas file")
    args = parser.parse_args()

    model = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    if args.mode == "visual":
        canvas = make_visual_canvas(model)
    elif args.mode == "cards":
        canvas = make_cards_canvas(model, formula=False)
    else:
        canvas = make_cards_canvas(model, formula=True)

    Path(args.output_canvas).write_text(json.dumps(canvas, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
