---
name: visual-learning-report
description: create a visual learning package from difficult articles, pdf chapters, book excerpts, papers, technical documents, or web clippings. use when the user wants an obsidian/llm-wiki compatible study package with multi-page chalkboard infographic html boards, a map html index, obsidian canvas learning boards, blackboard-colored canvas concept cards, formula canvas cards with obsidian latex and plain-language explanations, ingest-ready markdown, and claude code commands. especially useful for optics, math-heavy technical material, business/investment/history essays, zhihu/wechat articles, and research notes without directly modifying wiki pages.
---

# Visual Learning Report

## Purpose

Transform one difficult source or selected section into a self-contained learning package that helps the user understand the material before it is ingested into an Obsidian-based LLM Wiki.

Preserve the user's wiki workflow: keep `raw/` as the immutable source layer, write learning artifacts under `report/visual-explain/<date--slug>/`, and never directly edit `wiki/` pages. Generate commands for the user's Claude Code workflow instead of executing wiki ingest automatically.

## Default Output Package

Create one folder per source:

```text
report/visual-explain/YYYY-MM-DD--source-slug/
├── README.md
├── map.html
├── blackboard-thumbs.png
├── blackboard/
│   ├── 01-core-question.html
│   ├── 02-basic-principles.html
│   ├── 03-derivation.html
│   ├── 04-impact.html
│   └── ... up to 08-*.html
├── visual.canvas
├── cards.canvas
├── formulas.canvas
├── ingest-ready.md
└── commands.md
```

`blackboard-thumbs.png` is optional when screenshot generation is unavailable, but reserve the filename and mention in README how to create it from `map.html` or screenshots.

Do not make `visual.html`, `diagrams.md`, or `cards.md` the primary outputs. If older workflows ask for these files, explain that V0.2.4 uses `map.html`, the `blackboard/` folder, and `.canvas` boards instead.

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
   - formulas with LaTeX and plain-language explanations
   - what the user should remember
5. Split the source into a logical chalkboard sequence. Default order: 问题 -> 原理 -> 推导 -> 影响 -> 工程 -> 拓展. Reorder only when the source logic demands it.
6. Create the report files listed above.
7. Do not create or modify `wiki/` pages. Put downstream instructions in `commands.md`.

## Visual Design Rules

### map.html

Create a visual navigation page that shows all blackboard pages as a readable thumbnail grid.

Requirements:

- title: `<source title> - 知识导览图`
- show 1 card per blackboard page, numbered in reading order
- each map card has: page number, board title, one-sentence purpose, 3-4 key phrases
- include a recommended reading path: `1 -> 2 -> 3 -> ...`
- style must match the blackboard theme: dark background, chalk borders, neon green/cyan/orange/purple/yellow accents
- do not cram all content from the source into `map.html`; it is a guide, not the report itself

### blackboard/*.html

Create multiple fixed-size chalkboard infographic pages, not one overpacked board.

Default per-page canvas size: `1920px × 1080px` unless the user requests otherwise. Use 16:9 so pages fit better in Obsidian and browsers.

Content limits per page:

- 5-8 core points per page, counting major bullets or visual blocks
- 3-5 panels per page
- maximum 5 bullets per panel
- maximum 22 Chinese characters or 9 English words per bullet line; if longer, split into two short bullets
- maximum 120 Chinese characters per panel body, excluding headings and formulas
- title max 24 Chinese characters; subtitle max 36 Chinese characters
- formulas max 2 display formulas per page
- no panel may rely on CSS overflow to hide text

Mandatory overflow prevention:

- Use fixed panel sizes and generous gutters.
- Set `box-sizing: border-box` globally.
- Use `overflow: hidden` only as a final safety guard; first reduce text or split into another board.
- Every panel must include `max-width`, `line-height`, and readable font sizes.
- If any panel would require text smaller than 24px, split the board.
- If arrows/labels cross text or panels, move them to whitespace or remove them.
- Do not place panels so their borders overlap. Maintain at least 28px gutter between panels.

Style target:

- like an educational chalkboard information poster, not a modern web page
- dark blackboard background with subtle chalk dust/grid texture
- chalk-like Chinese title, hand-drawn borders, arrows, doodle icons, and grouped panels
- visual logic first: the page should feel like a teacher explaining one chapter of the knowledge map
- avoid glossy cards, modern SaaS gradients, hero sections, or web landing-page structure
- Obsidian-inspired accents:
  - neon green `#8bd93f` for concepts/mechanisms
  - cyan/blue `#38d9ff` for formulas/math
  - orange/red `#ff9f43` / `#ff5c5c` for core questions, contradictions, and warnings
  - purple `#b197fc` for ambiguity/limits
  - warm yellow `#ffe066` for examples, analogies, and memory anchors
  - chalk white `#f1f3f5` for main text
- Use inline CSS only; avoid external dependencies.
- Preserve LaTeX as Obsidian/MathJax-friendly text and show important formulas in chalk boxes.

Recommended board sequence:

```text
01 核心问题：为什么这篇材料值得学？
02 基本原理：最少必须懂的概念/公式。
03 推导链路：作者如何从前提走到结论。
04 影响机制：这个结论改变了什么判断。
05 工程/实践：如何应用、检查、落地。
06 易错点与自检：最容易误解的地方。
07 拓展关系：相关概念、反例、后续问题。
08 总复习：一页记忆路线图。
```

Only create as many pages as needed. Do not exceed 8 pages.


### Zero-Overflow Blackboard Rules (V0.2.3)

The user's top priority is that every blackboard panel must display all text completely. Treat clipping, text touching borders, or text hidden behind the next panel as a failure.

Use a conservative "air-first" layout:

- Prefer 2-4 panels per page. Use 5 panels only for very short content.
- Prefer 3-6 core points per page. The old 5-8 range is a maximum, not a target.
- Leave at least 44px gutter between all panels and at least 64px from board edges.
- Use `overflow: visible` during drafting and only switch the final `.board` to `overflow:hidden`; never set `.panel { overflow:hidden; }` because it hides failures.
- Every `.panel` must have `min-height` large enough for its text. Do not rely on fixed small boxes.
- If any panel contains a formula, give it at least 360px height.
- Use short chalk phrases instead of paragraphs. Convert long explanations into multiple boards.
- Body text max 22px-26px depending on density, but never below 22px.
- Use `word-break: break-word; overflow-wrap:anywhere;` for mixed Chinese/English/formulas.
- Use `ul { margin:0; padding-left:1.1em; }` and keep bullet spacing compact.
- Avoid large decorative labels such as “所以?” if they reduce text space. Put them only in clear whitespace.
- After drafting a board, perform a mental layout audit: check every panel's bottom padding, right padding, and whether the last bullet/formula is fully visible. If not, split the board.

Recommended safe templates:

1. **Three-card chain**: three equal cards in one row plus one wide conclusion card.
2. **Two-by-two**: four equal cards, no extra bottom label unless there is ample space.
3. **Formula board**: left intuition, middle formula, right variables, bottom meaning/trap.
4. **Comparison board**: two tall columns plus one full-width key distinction.

When content exceeds the template, create `blackboard/NN-extra-*.html` rather than shrinking or clipping.


### Zero-Overflow Blackboard Rules (V0.2.4)

The user repeatedly observed text being cut by panel borders. From this version onward, blackboard generation must use a strict layout-first workflow. Treat any clipped text, text touching borders, or text hidden behind another panel as a critical failure.

#### Required layout workflow

1. **Choose a safe template first.** Use only one of the fixed templates from `references/blackboard-infographic-style.md`: 2x2, 3-card chain, formula teaching board, comparison board, or vertical 3+1. Do not freestyle panel coordinates for dense boards.
2. **Calculate a text budget before writing.** For each panel, decide the maximum number of text lines it can safely hold. Then write content under that budget.
3. **Split before shrinking.** If the content exceeds the line budget, create another blackboard page. Never reduce body text below 24px to make content fit.
4. **Reserve bottom safety space.** Keep the bottom 120px of the board mostly empty unless using a short footer. Obsidian and browser chrome can visually crop the lower edge.
5. **Prefer fewer panels.** Default to 3 panels plus one conclusion. Use 5 panels only when each panel has very little text.
6. **Never put a long panel in a short box.** A panel with 4+ bullets or a formula must be at least 360px high. A panel with a table must be at least 460px high or moved to a separate page.
7. **No hidden overflow.** Do not set `overflow:hidden` on `.panel`, `.panel-body`, `li`, or `p`. Only the outer `.board` may use `overflow:hidden`.

#### Hard per-panel text budgets

Use these as maximums, not targets:

- Small panel `520x340`: heading + 3 bullets, each bullet <= 18 Chinese characters or <= 8 English words.
- Medium panel `760x360`: heading + 4 bullets, each bullet <= 22 Chinese characters or <= 10 English words.
- Large panel `820x400`: heading + 5 bullets OR 1 formula + 3 bullets.
- Full-width conclusion `1560x220`: heading + 2 short lines only.
- Table panel: max 3 rows x 3 columns; otherwise split into a dedicated table board.

If a concept needs more explanation, move details to `cards.canvas` or the next blackboard page. Blackboard pages should teach the path, not store every detail.

#### CSS requirements

Every `blackboard/*.html` page must use:

```css
* { box-sizing: border-box; }
.panel {
  position: absolute;
  overflow: visible;
  padding: 24px 32px 34px;
  line-height: 1.38;
}
.panel h2 { margin: 0 0 14px; line-height: 1.15; }
.panel p, .panel li {
  margin: 7px 0;
  line-height: 1.34;
  overflow-wrap: anywhere;
  word-break: break-word;
}
ul { margin: 0; padding-left: 1.05em; }
.formula-box {
  max-width: 100%;
  white-space: normal;
  overflow-wrap: anywhere;
}
```

Avoid absolute text labels over panels. Put arrows in gutters only. If an arrow or label overlaps a panel, remove it.

#### Mandatory self-audit before finalizing each board

For every board, explicitly check:

- Does any bullet continue below the panel border? If yes, split the page.
- Is the last bullet at least 28px above the bottom border? If no, split the page.
- Does any formula touch the right border? If yes, move it to a formula board or wrap it in a larger box.
- Are there more than 4 dense panels? If yes, split the page.
- Would this board still be readable at 70% zoom in Obsidian? If no, split the page.

When unsure, create one more board. More pages are better than clipped content.

### visual.canvas

Create the main Obsidian learning whiteboard. It should be a usable learning map, not just links to files.

Default layout:

- center node: source title and one-sentence thesis
- top row: core question, why it matters, final takeaway
- middle row: mechanism / argument chain cards
- lower row: examples, limitations, review questions
- bottom row: file nodes linking to `map.html`, `blackboard/01-*.html`, `cards.canvas`, `formulas.canvas`, and `ingest-ready.md`

Use Canvas for large diagrams and logical relationships. Avoid Mermaid as the main diagram medium unless the user explicitly asks.

### cards.canvas

Make this the primary concept-card output. Put all concept cards on an Obsidian Canvas as separate cards.

Blackboard color requirements:

- Do not make every card green.
- Use the same palette as `blackboard/*.html` by card type:
  - concept/mechanism cards: green
  - formula/math cards embedded in cards: blue/cyan
  - core problem, contradiction, trap: red/orange
  - example/analogy/application: yellow
  - limitation/ambiguity/risk: purple
  - source/review cards: gray/default
- When using the helper script, include `kind` or `color` in card JSON so cards get mixed colors.

Card sizing rules:

- default `card_width`: 620
- default `card_height`: 420
- default columns: 3
- default gaps: 120px horizontal, 120px vertical
- if a card has a formula or >180 Chinese characters, set width 680-760 and height 460-560
- never let text run outside the visible card area; split long cards into two cards using suffixes like `定义` and `例子/易混点`

Each card should follow this structure, using Obsidian formula syntax:

```markdown
# 概念卡：中文名 / Original Term

## 定义
...

## 公式
$inline$ 或
$$
block_latex
$$

## 直觉
...

## 例子
...

## 容易混淆
...

## 相关概念
[[concept-a]] · [[concept-b]]

## 置信度
extracted | inferred | ambiguous
```

Prefer section headings over dense bullets so Obsidian Canvas renders cleanly.

### formulas.canvas

Create this when formulas or mathematical relationships exist. If there are no formulas, create a small canvas with one note saying no core formulas were extracted.

Each formula card should use Obsidian formula syntax:

```markdown
# 公式卡：公式名 / Original Term

$$
<latex>
$$

## 人话解释
...

## 变量解释
- $x$：...

## 直觉图像
...

## 工程/实践意义
...

## 常见误解
...

## 来源位置
...
```

## File Requirements

### README.md

Make this the entry point. Include:

- source title and source path or URL
- recommended reading order for the package
- a small table listing every `blackboard/*.html` page and its purpose
- mention `map.html` as the first visual entry
- what each generated file is for
- whether `blackboard-thumbs.png` was generated or must be saved manually from `map.html`
- next action: review the package, then run the commands in `commands.md`

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
- Prefer Canvas for large diagrams and card collections; use Mermaid only for tiny local snippets when specifically requested.

## Using the Canvas Helper

Use `scripts/create_canvas.py` when a deterministic canvas layout helps. The helper can create:

- `visual.canvas` from a structured learning-board JSON model
- `cards.canvas` from concept-card JSON
- `formulas.canvas` from formula-card JSON

Run examples:

```bash
python scripts/create_canvas.py visual model.json visual.canvas
python scripts/create_canvas.py cards cards.json cards.canvas
python scripts/create_canvas.py formulas formulas.json formulas.canvas
```

For `cards.canvas`, include `kind` or `color` for every card when possible:

```json
{"title":"彗差","kind":"risk","definition":"..."}
{"title":"净灵敏度","kind":"formula","latex":"S_{lens} \\propto \\phi_1^2 + k\\phi_2^2"}
```

## Quality Checklist

Before finishing, verify:

- The report folder name is stable and file-system safe.
- `map.html` links to all blackboard pages in reading order.
- There are no more than 8 blackboard pages.
- Each blackboard page is a 1920×1080 chalkboard infographic and uses a safe fixed template with no clipped text; prefer 3-6 core points and split aggressively.
- No blackboard panel text crosses, touches, or overflows outside its border; last visible line has at least 28px bottom clearance.
- Blackboard pages use chalkboard background, hand-drawn panels, arrows, and dense-but-readable educational layout.
- Important original terms are preserved and explained in Chinese.
- LaTeX formulas are preserved using Obsidian-friendly `$...$` or `$$...$$` syntax.
- `visual.canvas` is a real learning map, not only a list of file links.
- `cards.canvas` contains separated concept cards in a grid, with mixed blackboard-inspired colors.
- `cards.canvas` card formulas use Obsidian formula syntax.
- `formulas.canvas` exists when formulas are present, and is valid even if no formulas are found.
- Canvas JSON files are valid.
- `commands.md` does not overwrite the user's original `raw/` file by accident.
- The final answer gives the user the package path or download link and highlights any missing artifact such as `blackboard-thumbs.png`.

## Bundled Resources

- `references/report-package-spec.md`: detailed file templates and report content rules.
- `references/blackboard-infographic-style.md`: chalkboard infographic visual rules and HTML skeleton.
- `references/canvas-layout-spec.md`: Obsidian Canvas layout and color conventions.
- `scripts/create_canvas.py`: helper script to generate Obsidian `.canvas` files from structured JSON.
