# Blackboard HTML Style Guide

## Visual direction

Create chalkboard teaching infographics, inspired by a teacher explaining a hard concept on a dark board.

Use:

- one `map.html` navigation board
- multiple focused `blackboard/*.html` boards
- dark graphite/blackboard background with subtle grid/dust texture
- chalk-like off-white body text
- neon green headings
- cyan formula accents
- orange/red warning or core question accents
- purple secondary accents
- hand-drawn-feeling borders, arrows, circles, and callouts
- compact diagrams and icons when they clarify the lesson

Avoid:

- generic web landing-page styling
- a long article page pretending to be a blackboard
- tiny text
- edge collisions and overlapping boxes
- trying to fit the whole source onto one board
- external CSS files

## Page size

Default each blackboard page to a 16:9 board such as 1920x1080. It may be responsive, but the first viewport should look like a complete infographic.

Recommended HTML wrapper:

```html
<body>
  <main class="board board-16x9">
    ...
  </main>
</body>
```

## map.html layout

`map.html` should act like a table of contents and thumbnail guide:

- title and one-sentence thesis
- a reading path ribbon
- 1 card per blackboard page
- each card links to `blackboard/NN-topic.html`
- include links to `visual.canvas`, `cards.canvas`, `formulas.canvas`, `ingest-ready.md`, and `commands.md`

## Blackboard board layout

Use a clear grid with 3-6 blocks. Typical layouts:

- 2x2 blocks plus a bottom memory anchor
- left-to-right chain with 4-6 blocks
- central formula with surrounding concept blocks
- warning/self-check board with red/orange callouts

Each board must include:

- board number and topic
- source title in small text
- 5-8 core points
- one-line memory anchor or takeaway

## Formula handling

Preserve formulas as LaTeX using Obsidian/Markdown syntax in visible text:

```html
<div class="formula">$$ S_{lens} \propto \phi^2 + k\phi^2 $$</div>
<p>人话解释：平方项意味着小偏差会被放大。</p>
```

Do not rely solely on MathJax rendering. The raw LaTeX should remain understandable.

## Collision prevention

Before finalizing, check mentally:

- Does every block have whitespace around it?
- Are arrows shorter than the page width?
- Are title and blocks inside the visible frame?
- Is any block touching another block?
- Would this still be readable in Obsidian's embedded browser?

If not, split into another board.
