# Blackboard HTML Style Guide

## Visual direction

Create a chalkboard teaching page, inspired by a teacher explaining a hard concept on a dark board.

Use:

- dark grid or blackboard background
- chalk-like off-white body text
- bright chalk accent headings
- boxed concept cards
- arrows and numbered steps
- compact top cover suitable for screenshot
- scrollable detail sections below

Avoid:

- generic blog styling
- tiny text
- too many colors
- decorative complexity that hides the argument
- external CSS files

## HTML skeleton

Use self-contained HTML with inline CSS. Include sections:

```html
<section class="cover">...</section>
<section class="map">...</section>
<section class="explain">...</section>
<section class="formulas">...</section>
<section class="cards">...</section>
<section class="questions">...</section>
```

## Formula handling

Preserve formulas as LaTeX:

```html
<div class="formula">$$ OPD = nL $$</div>
<p>人话解释：...</p>
```

If MathJax is included, make it optional and keep the raw LaTeX visible enough for offline use.

## Cover section layout

The cover should contain:

- title
- core question
- thesis
- 3-5 key nodes
- reading path arrows
- source metadata in small text

It must be understandable as a standalone screenshot.
