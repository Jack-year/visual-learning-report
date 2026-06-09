# Obsidian Canvas Style Guide

## Purpose

Use Canvas as the main editable diagram surface. Do not rely on large Mermaid diagrams for complex relationships because they often crop or become unreadable in Obsidian.

## Canvas files

Generate:

- `visual.canvas`: overview learning board and file navigator.
- `cards.canvas`: all concept cards as separate nodes.
- `formulas.canvas`: formula cards when formulas exist.

## Color conventions

Use Obsidian Canvas color IDs consistently:

- Core question / risk / warning: `1`
- Key concept / principle: `4`
- Formula / derivation: `5`
- Example / application / engineering: `6`
- Limitation / uncertainty: `3`
- Neutral file links and notes: omit color or use default

If the runtime or Obsidian theme interprets colors differently, prioritize consistency of category over exact hue.

## Layout conventions

### visual.canvas

- Center node: source title and thesis.
- Top row: core question and reading path.
- Middle row: principle, derivation, impact.
- Lower row: engineering, limitations, review questions.
- Bottom row: file nodes linking to generated artifacts.
- Use edges with labels like `提出问题`, `依赖`, `推导`, `导致`, `落地`, `复习`.

### cards.canvas

Create a grid of card nodes.

- Card width: 520-640.
- Card height: 360-520 depending on content.
- 3 cards per row for ordinary cards.
- Use a larger height for formula-heavy cards.
- Avoid overlap; use at least 80 px horizontal and vertical spacing.

### formulas.canvas

Use one formula per node.

- Put the formula near the top.
- Use `$$...$$` display math.
- Add variables and human explanation below.
- Link related formulas with edges when there is a derivation relation.

## Node text rules

Canvas text nodes support Markdown. Use:

- `#` or `##` for node titles.
- bold labels for sections.
- `$...$` for inline formulas.
- `$$...$$` for display formulas.
- `[[wikilink]]` only as suggestions, not as claims that pages already exist.

## File nodes

For generated files, use Canvas file nodes when possible:

```json
{
  "id": "file-map",
  "type": "file",
  "file": "map.html",
  "x": 0,
  "y": 900,
  "width": 360,
  "height": 80
}
```

Use relative paths from the report folder.
