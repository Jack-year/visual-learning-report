#!/usr/bin/env python3
"""Generate an Obsidian Canvas file from a compact JSON model.

Input JSON format:
{
  "title": "...",
  "nodes": [
    {"id": "core", "label": "核心问题", "text": "..."},
    {"id": "concepts", "label": "核心概念", "items": ["A", "B"]}
  ],
  "files": [
    {"path": "visual.html", "label": "Visual report"}
  ],
  "edges": [
    {"from": "center", "to": "core", "label": "asks"}
  ]
}
"""
import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


def node_text(node: Dict[str, Any]) -> str:
    label = node.get("label", "")
    text = node.get("text", "")
    items = node.get("items", [])
    lines: List[str] = []
    if label:
        lines.append(f"# {label}")
    if text:
        lines.append(str(text))
    if items:
        lines.extend(f"- {item}" for item in items)
    return "\n".join(lines).strip() or "空节点"


def build_canvas(model: Dict[str, Any]) -> Dict[str, Any]:
    title = model.get("title", "Visual Learning Report")
    canvas_nodes: List[Dict[str, Any]] = [
        {
            "id": "center",
            "type": "text",
            "text": f"# {title}\n\n可视化学习报告",
            "x": 0,
            "y": 0,
            "width": 420,
            "height": 220,
        }
    ]
    canvas_edges: List[Dict[str, Any]] = []

    positions = [
        (-520, -320), (0, -360), (520, -320),
        (-560, 0), (560, 0),
        (-520, 320), (0, 380), (520, 320),
    ]

    for idx, node in enumerate(model.get("nodes", [])):
        node_id = str(node.get("id", f"node-{idx}"))
        x, y = positions[idx % len(positions)]
        canvas_nodes.append({
            "id": node_id,
            "type": "text",
            "text": node_text(node),
            "x": x,
            "y": y,
            "width": 380,
            "height": 240,
        })
        canvas_edges.append({
            "id": f"edge-center-{node_id}",
            "fromNode": "center",
            "toNode": node_id,
        })

    file_y = 680
    for idx, file_node in enumerate(model.get("files", [])):
        file_id = f"file-{idx}"
        canvas_nodes.append({
            "id": file_id,
            "type": "file",
            "file": file_node["path"],
            "x": -520 + idx * 360,
            "y": file_y,
            "width": 320,
            "height": 180,
        })
        canvas_edges.append({
            "id": f"edge-center-{file_id}",
            "fromNode": "center",
            "toNode": file_id,
            "label": file_node.get("label", "file"),
        })

    for idx, edge in enumerate(model.get("edges", [])):
        canvas_edges.append({
            "id": f"custom-edge-{idx}",
            "fromNode": edge["from"],
            "toNode": edge["to"],
            **({"label": edge["label"]} if edge.get("label") else {}),
        })

    return {"nodes": canvas_nodes, "edges": canvas_edges}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an Obsidian Canvas JSON file.")
    parser.add_argument("input_json", help="Path to canvas model JSON")
    parser.add_argument("output_canvas", help="Path to output .canvas file")
    args = parser.parse_args()

    model = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    canvas = build_canvas(model)
    Path(args.output_canvas).write_text(
        json.dumps(canvas, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
