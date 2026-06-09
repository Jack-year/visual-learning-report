# Report Package Spec

Create one folder per source under:

```text
report/visual-explain/YYYY-MM-DD--source-slug/
```

## Required Files

```text
README.md
map.html
blackboard-thumbs.png
blackboard/
  01-core-question.html
  02-basic-principles.html
  03-derivation.html
  ... up to 08-*.html
visual.canvas
cards.canvas
formulas.canvas
ingest-ready.md
commands.md
```

`blackboard-thumbs.png` is optional when screenshot generation is not available, but the filename should be reserved and mentioned in README.

## README.md Template

```markdown
# <title> 可视化学习包

- 来源：<raw path or URL>
- 类型：article | book | paper | docs | clipping | note
- 生成日期：YYYY-MM-DD

## 推荐阅读顺序

1. 打开 `map.html`，先看所有黑板页的导览。
2. 按顺序阅读 `blackboard/01-*.html` 到最后一页。
3. 打开 `visual.canvas`，按节点关系复习逻辑。
4. 打开 `cards.canvas`，逐张复习概念卡。
5. 如果有公式，打开 `formulas.canvas`。
6. 审核 `ingest-ready.md` 后，按 `commands.md` 执行 ingest。

## 黑板页目录

| 页码 | 文件 | 作用 |
|---|---|---|
| 01 | `blackboard/01-core-question.html` | 核心问题与学习入口 |
| 02 | `blackboard/02-basic-principles.html` | 基本原理 |

## 文件说明

- `map.html`：黑板页导览图。
- `blackboard/`：多张 1920×1080 黑板信息图，每张聚焦 5-8 个核心点。
- `blackboard-thumbs.png`：导览缩略图。若未生成，请从 `map.html` 手动导出。
- `visual.canvas`：总学习白板。
- `cards.canvas`：概念知识卡片白板，配色参考黑板页。
- `formulas.canvas`：公式卡片白板。
- `ingest-ready.md`：适合放入 raw/ 的摄入素材。
- `commands.md`：Claude Code 后续命令。
```

## ingest-ready.md Template

```markdown
---
title: "..."
source: "..."
source_type: article | book | paper | docs | clipping | note
author: "..."
published: "..."
created: "YYYY-MM-DD"
language: "..."
---

# <title>

## 来源摘要

## 原文或忠实摘录/大纲

## 提取概念

## 提取公式

## 关键声明

- ... [extracted]
- ... [inferred]
- ... [ambiguous]

## 待补充/疑问
```

## commands.md Rules

- If the original source already lives in `raw/`, run ingest on that original raw file.
- If the user wants the structured digest ingested, copy `ingest-ready.md` into the matching `raw/` directory.
- Never overwrite an existing raw file without telling the user.


## V0.2.4 blackboard split policy

When generating `blackboard/*.html`, split content aggressively. Prefer extra pages over dense panels. Any board with clipped text is invalid. If a page has technical formulas, tables, or mixed Chinese/English terminology, reduce to 3-4 panels and 3-6 core points. Use `cards.canvas` and `formulas.canvas` for details that do not fit cleanly on the blackboard page.
