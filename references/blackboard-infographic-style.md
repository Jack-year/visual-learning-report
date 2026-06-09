# Blackboard Infographic Style

Use this reference when creating `map.html` and `blackboard/*.html`.

## Goal

Create multiple chalkboard information graphics that explain the source like a teacher drawing on a blackboard. The boards should resemble educational posters, not web pages.

Default per-board size: `1920px` wide by `1080px` tall.

## Multi-board Strategy

Never force a whole article/chapter into one board.

- Split into 2-8 boards depending on complexity.
- Each board focuses on one logical step.
- Each board contains 5-8 core points, 3-5 panels, and at most 2 formulas.
- Use `map.html` to show all boards in sequence.

Default sequence:

```text
01 core question
02 basic principles
03 derivation / argument chain
04 impact / mechanism
05 engineering / application
06 mistakes / self-check
07 extensions / related concepts
08 review map
```

## Visual Language

- Background: near-black or dark charcoal board with subtle noise/grid/chalk dust.
- Typography: large chalk-like Chinese title, readable sans-serif body, short phrases.
- Panels: hand-drawn-looking boxes, dashed chalk borders, rounded chalk bubbles.
- Arrows: chalk arrows connecting panels, placed in whitespace.
- Icons: simple emoji or line doodles, used sparingly.
- Colors:
  - neon green `#8bd93f` for concepts
  - cyan `#38d9ff` for formulas/math
  - orange/red `#ff9f43` / `#ff5c5c` for core questions and risks
  - purple `#b197fc` for ambiguity/limits
  - warm yellow `#ffe066` for examples and analogies
  - chalk white `#f1f3f5` for main text

## Hard Layout Constraints

Prevent overflow and overlapping text.

- Board: exactly `width:1920px; height:1080px; overflow:hidden`.
- Use `* { box-sizing: border-box; }`.
- Keep at least `28px` gutters between panels.
- Minimum body font size: `24px`.
- Preferred body font size: `26-30px`.
- Heading font size: `34-46px`.
- Title font size: `58-72px`.
- Panel line-height: `1.35-1.5`.
- Maximum 5 bullets per panel.
- Maximum 120 Chinese characters per panel body.
- Maximum 22 Chinese characters per bullet line; rewrite long bullets as short phrases.
- If a panel needs more text, split it into another board. Do not shrink text below 24px.
- If formula or Chinese text touches a border, increase panel size or split the board.
- Never place a label like “所以?” across panel borders unless it is intentionally in whitespace.

## Recommended HTML Skeleton

```html
<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>...</title>
<style>
  * { box-sizing: border-box; }
  html, body { margin:0; background:#0d0f0e; }
  .board {
    width:1920px; height:1080px; position:relative; overflow:hidden;
    padding:54px 64px;
    background:
      radial-gradient(circle at 20% 15%, rgba(255,255,255,.05), transparent 22%),
      linear-gradient(rgba(255,255,255,.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,.03) 1px, transparent 1px),
      #151716;
    background-size:auto, 32px 32px, 32px 32px, auto;
    color:#f1f3f5;
    font-family:"LXGW WenKai","Noto Sans SC","Microsoft YaHei",sans-serif;
  }
  .title { position:absolute; left:64px; top:42px; font-size:66px; line-height:1.05; color:#ffe066; }
  .subtitle { position:absolute; left:68px; top:118px; font-size:28px; color:#b2f2bb; }
  .panel {
    position:absolute; padding:26px 30px;
    border:4px solid rgba(241,243,245,.76); border-radius:22px;
    background:rgba(0,0,0,.22); overflow:visible;
  }
  .panel h2 { margin:0 0 14px; font-size:34px; line-height:1.2; color:#8bd93f; }
  .panel p, .panel li { font-size:26px; line-height:1.42; margin:8px 0; overflow-wrap:anywhere; word-break:break-word; }
  .panel ul { margin:0; padding-left:26px; }
  .core { border-color:#ff9f43; }
  .formula { border-color:#38d9ff; }
  .risk { border-color:#ff5c5c; }
  .limit { border-color:#b197fc; }
  .example { border-color:#ffe066; }
  .concept { border-color:#8bd93f; }
  .accent-green { color:#8bd93f; }
  .accent-cyan { color:#38d9ff; }
  .accent-orange { color:#ff9f43; }
  .accent-red { color:#ff5c5c; }
  .accent-purple { color:#b197fc; }
  .accent-yellow { color:#ffe066; }
  .formula-box { font-size:30px; color:#38d9ff; padding:12px 16px; border:2px dashed #38d9ff; border-radius:12px; display:inline-block; }
  .arrow { position:absolute; color:rgba(241,243,245,.65); font-size:48px; line-height:1; }
</style>
</head>
<body><main class="board">...</main></body>
</html>
```


## Zero-Overflow Layout Contract

The blackboard aesthetic is secondary to legibility. A board with clipped text is invalid. Use this contract for every `blackboard/*.html` page:

1. **Draft with visible overflow**: `.panel { overflow: visible; }` while authoring. Clipped text must be visible as a problem.
2. **Final panels do not hide content**: avoid `.panel { overflow:hidden; }`. Only the outer `.board` may use `overflow:hidden` to maintain screenshot boundaries.
3. **Budget before writing**:
   - small panel: heading + 3 bullets max
   - medium panel: heading + 4 bullets max
   - large panel: heading + 5 bullets or 1 formula + 3 bullets max
   - full-width panel: heading + 2 short lines max
4. **Split aggressively**: if a panel needs more than 5 bullets, or if a bullet needs more than 2 visual lines, create another board.
5. **No border collisions**: text must have at least 22px internal bottom padding and 24px right padding after the final visible line.
6. **Formula safety**: formulas often render wider/taller than expected. Put each important formula in its own formula box or formula-focused board; do not place long formulas inside crowded bullets.
7. **Browser and Obsidian safe width**: design each page so it still reads when zoomed to fit width. Avoid text near the extreme bottom 80px because Obsidian UI can cover it.

Use fewer points per page when the material is technical. For math/optics, 3-5 panels and 4-6 core points is usually better than 8 points.

### Safe 1920x1080 coordinates

Use these coordinate systems instead of freehand placement. They include enough whitespace to avoid clipping.

**2 x 2 board**

```text
Title: x=64 y=42 w=1792 h=96
Panel A: x=80  y=170 w=820 h=330
Panel B: x=1020 y=170 w=820 h=330
Panel C: x=80  y=570 w=820 h=330
Panel D: x=1020 y=570 w=820 h=330
Footer:  x=80  y=930 w=1760 h=90 optional, only for 1-2 short lines
```

**3-card chain + conclusion**

```text
Panel A: x=80   y=200 w=520 h=360
Panel B: x=700  y=200 w=520 h=360
Panel C: x=1320 y=200 w=520 h=360
Conclusion: x=180 y=660 w=1560 h=250
```

**Formula teaching board**

```text
Intuition: x=80   y=190 w=520 h=360
Formula:   x=700  y=190 w=520 h=360
Variables: x=1320 y=190 w=520 h=360
Meaning:   x=180  y=650 w=1560 h=260
```

**Comparison board**

```text
Left column:  x=80   y=180 w=780 h=560
Right column: x=1060 y=180 w=780 h=560
Key difference: x=180 y=800 w=1560 h=180
```

Do not add extra panels beyond these templates unless the text is extremely short.

## Panel Layout Patterns

Use these instead of freehand placement.

### 3 panel chain + conclusion

```text
[title]
[panel 1] -> [panel 2] -> [panel 3]
[wide conclusion panel]
```

### 2 x 2 board + takeaway

```text
[title]
[panel 1] [panel 2]
[panel 3] [panel 4]
[wide memory anchor]
```

### Formula teaching board

```text
[title]
[left intuition] [center formula] [right variable meaning]
[bottom engineering meaning / common trap]
```

## map.html

`map.html` should be a guide page with cards for all boards. It may be larger or scrollable, but still use the same chalkboard palette. It should not repeat all content.

Each map card:

- number
- board title
- one-sentence purpose
- 3-4 keywords
- link to the corresponding `blackboard/*.html`

## Anti-patterns

Avoid:

- one giant overpacked board for a whole chapter
- SaaS landing page hero layouts
- glossy gradient cards
- long paragraphs inside panels
- text touching or crossing panel borders
- arrows passing through text
- Mermaid diagrams embedded as the main visual
- tiny text that cannot be read when zoomed out

## V0.2.4 Anti-Clipping Upgrade

This section overrides any earlier density guideline when there is a conflict. The user prefers extra pages over clipped text.

### Non-negotiable rule

A blackboard page is invalid if any text is hidden, cut off, covered by a border, or too close to the panel edge. Split the content into another page instead of shrinking text or forcing a denser layout.

### Page density target

- Default target: 3-6 core points per page.
- Maximum: 8 only when every point is a short phrase.
- Default panel count: 3 panels + 1 conclusion panel.
- Maximum dense panels: 4. Use 5 only for very short labels.

### Extra-safe templates

Use these exact dimensions for technical content. Do not reduce them.

**Template A: 3 cards + conclusion**

```text
Title safe zone: y=30..140
A: x=80   y=180 w=520 h=390
B: x=700  y=180 w=520 h=390
C: x=1320 y=180 w=520 h=390
Conclusion: x=180 y=660 w=1560 h=250
Bottom safe zone: y=940..1080, no important text
```

**Template B: 2 x 2 spacious**

```text
A: x=80   y=170 w=820 h=360
B: x=1020 y=170 w=820 h=360
C: x=80   y=590 w=820 h=360
D: x=1020 y=590 w=820 h=360
No footer unless it is one short line.
```

**Template C: formula board**

```text
Intuition: x=80   y=180 w=520 h=390
Formula:   x=700  y=180 w=520 h=390
Variables: x=1320 y=180 w=520 h=390
Meaning:   x=180  y=660 w=1560 h=250
```

**Template D: comparison board**

```text
Left:  x=80   y=170 w=780 h=610
Right: x=1060 y=170 w=780 h=610
Key distinction: x=180 y=830 w=1560 h=160
```

### Text-budget table

| Panel size | Maximum content | Action if exceeded |
|---|---|---|
| 520x390 | heading + 3 bullets | split |
| 780x610 | heading + 7 short bullets | split |
| 820x360 | heading + 4 bullets | split |
| 1560x250 | heading + 2 short lines | split |
| formula panel | one display formula + 2 bullets | move formula to formulas.canvas or next board |

### Authoring discipline

- Convert paragraphs into chalk phrases.
- Avoid nested bullets on blackboards.
- Avoid tables except in dedicated table boards.
- Avoid decorative oversized text such as “所以?” unless there is guaranteed whitespace.
- If using Chinese + English terms, put English in parentheses only when essential; otherwise move original term to `cards.canvas`.
- Do not use CSS transforms or negative margins for text.
- Keep panel `padding-bottom` at least 34px.

### Final CSS patch

Use this patch on every blackboard page:

```css
.panel {
  overflow: visible;
  padding: 24px 32px 36px;
}
.panel h2 {
  font-size: 34px;
  line-height: 1.15;
  margin: 0 0 14px;
}
.panel p, .panel li {
  font-size: 25px;
  line-height: 1.34;
  margin: 7px 0;
  overflow-wrap: anywhere;
  word-break: break-word;
}
.panel .small { font-size: 22px; line-height: 1.32; }
.formula-box {
  max-width: 100%;
  white-space: normal;
  overflow-wrap: anywhere;
  word-break: break-word;
}
```

Use `.small` sparingly for captions only, never for the main explanation.
