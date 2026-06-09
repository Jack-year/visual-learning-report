---
name: visual-learning-report
description: create a visual learning package from difficult articles, pdf chapters, book excerpts, papers, technical documents, or web clippings. use when the user wants an obscidian/llm-wiki compatible study report with a blackboard-style html explanation, concept cards, formula cards with latex and plain-language explanations, mermaid diagrams, an obsidian canvas file, ingest-ready markdown, and claude code commands. especially useful for learning optics, math-heavy technical material, business/investment/history essays, zhihu/wechat articles, and research notes without directly modifying wiki pages.
---

# Visual Learning Report

## Purpose

Transform one difficult source or selected section into a self-contained learning package that helps the user understand the material before it is ingested into an Obsidian-based LLM Wiki.

This skill must preserve the user's wiki workflow: keep `raw/` as the immutable source layer, write learning artifacts under `report/visual-explain/<date--slug>/`, and never directly edit `wiki/` pages. Generate commands for the user's Claude Code workflow instead of executing wiki ingest automatically.

## Default Output Package

Create one folder per source:

```text
report/visual-explain/YYYY-MM-DD--source-slug/
├── README.md
├── visual.html
├── visual.canvas
├── cover.png
├── diagrams.md
├── cards.md
├── formulas.md
├── ingest-ready.md
└── commands.md
```

If image generation or screenshot capture is unavailable, still create `visual.html` and include instructions in `README.md` for saving the top overview section as `cover.png`.

## Workflow

1. Identify the source type: article, pdf chapter, book excerpt, paper section, technical document, web clipping, or pasted text.
2. Extract metadata where available: title, source path or URL, author, published date, created date, source type, and language.
3. Preserve important original terms in their source language, then explain them in Chinese. For technical material, keep canonical English terms beside Chinese translations.
4. Build the learning model:
   - one-sentence thesis
   - core question
   - why it matters
   - reading map
   - key concepts
   - argument chain
   - examples or applications
   - limitations, disputes, and uncertainty
   - what the user should remember
5. Create the report files listed above.
6. Do not create or modify `wiki/` pages. Put downstream instructions in `commands.md`.

## File Requirements

### README.md

Make this the entry point. Include:

- source title and source path or URL
- recommended reading order for the package
- what each generated file is for
- whether `cover.png` was generated or must be saved manually from `visual.html`
- next action: review the package, then run the commands in `commands.md`

### visual.html

Create a polished, self-contained blackboard-style learning page. Default to a scrollable long page with a screenshot-friendly one-screen overview at the top.

Structure:

1. blackboard cover section: title, core question, thesis, three to five key nodes, and a visual reading path
2. layered explanation: background -> concepts -> argument chain -> examples -> limitations -> memory anchors
3. formula explanation section when formulas exist
4. concept cards section
5. review questions section
6. source and uncertainty notes

Style rules:

- Use a dark blackboard background, chalk-like text, accent colors, boxes, arrows, and hand-drawn-feeling layout.
- Keep the page readable in Obsidian or a browser.
- Use inline CSS only; avoid external dependencies.
- Preserve LaTeX formulas as MathJax-compatible text. If using MathJax CDN is not appropriate for offline use, also include plain LaTeX source immediately next to formulas.
- Do not over-pack the cover. The cover is for orientation; the scrollable body is for depth.

### visual.canvas

Generate an Obsidian Canvas JSON file. Use a center node and surrounding nodes:

- center theme
- core question
- key concepts
- argument chain
- formulas
- examples/applications
- limitations
- review questions
- links to generated markdown files and `visual.html`

When possible, generate this from a small structured JSON model using `scripts/create_canvas.py`.

### diagrams.md

Include Mermaid diagrams. Prefer three diagram types when useful:

- logic flowchart
- concept relationship graph
- cause-effect graph or timeline

Keep diagrams concise and editable. Add a short Chinese explanation before each diagram.

### cards.md

Create concept, question, and review cards. Use this structure for concept cards:

```markdown
## 概念卡：<concept> / <original term>

- 定义：
- 直觉：
- 例子：
- 容易混淆：
- 相关概念：[[concept-a]], [[concept-b]]
- 置信度：extracted | inferred | ambiguous
```

### formulas.md

Create this file even if there are no formulas; in that case write “本材料未提取到核心公式”. For each formula, use:

```markdown
## <公式名> / <original term>

$$
<latex>
$$

- 人话解释：
- 变量解释：
- 直觉图像：
- 工程/实践意义：
- 常见误解：
- 来源位置：
```

### ingest-ready.md

Create a cleaned, structured Markdown version suitable for putting under `raw/articles/`, `raw/books/`, `raw/papers/`, or `raw/docs/`. It should not be a wiki page and should not invent knowledge. Include:

- source metadata
- brief source summary
- original material or faithful excerpt/outline
- extracted concepts
- extracted formulas
- extracted claims with `[extracted]`, `[inferred]`, or `[ambiguous]`
- open questions

### commands.md

Generate copy-pasteable shell and Claude Code commands. Adapt `raw/` target based on source type:

```bash
# copy ingest-ready material into raw
cp "report/visual-explain/YYYY-MM-DD--slug/ingest-ready.md" "raw/articles/YYYY-MM-DD--slug.md"

# run ingest in claude code
claude "请读取 CLAUDE.md，然后对 raw/articles/YYYY-MM-DD--slug.md 执行 ingest"

# optional lint after review
claude "请读取 prompt/lint.md，对 wiki/ 执行 lint 检查"
```

If the user already placed the original source in `raw/`, do not copy over it. Instead point Claude Code at that existing raw file and mention that the visual report is supplemental.

## Obsidian and LLM Wiki Compatibility

Follow these conventions:

- `raw/` stores original or faithful source material only.
- `report/visual-explain/` stores learning reports and generated artifacts.
- `wiki/` is maintained by the user's ingest workflow; do not write directly to it.
- Use `[[wikilink]]` suggestions in cards, but avoid pretending pages already exist unless they are known.
- Mark uncertainty instead of turning inference into fact.
- Prefer one source per report folder.

## Quality Checklist

Before finishing, verify:

- The report folder name is stable and file-system safe.
- The visual page has a top cover and deeper scrollable explanation.
- Important original terms are preserved and explained in Chinese.
- LaTeX formulas are preserved and explained plainly.
- Mermaid diagrams are editable.
- Canvas JSON is valid.
- `commands.md` does not overwrite the user's original `raw/` file by accident.
- The final answer gives the user the package path or download link and highlights any missing artifact such as `cover.png`.

## Bundled Resources

- `references/report-package-spec.md`: detailed file templates and report content rules.
- `references/blackboard-html-style.md`: visual style and HTML layout guidance.
- `scripts/create_canvas.py`: helper script to generate an Obsidian `.canvas` file from structured JSON.
