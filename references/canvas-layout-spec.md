# Canvas Layout Spec

Use this reference when creating Obsidian `.canvas` files.

## General Rules

- Canvas is the primary medium for diagrams and knowledge cards.
- Use separate text nodes for each card.
- Keep nodes spaced generously so Obsidian does not feel cluttered.
- Prefer section headings and compact lines over paragraphs.
- Use colors consistently and match the blackboard palette as closely as Obsidian Canvas permits.

## Colors

Obsidian Canvas supports preset color labels, not exact CSS hex colors. Map the blackboard palette to Canvas labels:

- red/orange: core question, contradictions, warnings, traps
- green: concepts, mechanisms, principles
- blue/cyan: formulas, variables, mathematical relationships
- yellow: examples, analogies, applications, memory anchors
- purple: limits, ambiguity, risks, disputes
- gray/default: source notes, review prompts, file links

Do not assign all concept cards the same color. Choose card color from its role.

## visual.canvas Layout

Use a large learning board:

```text
            [核心问题]       [为什么重要]       [最终结论]

[背景/上下文]        [中心主题 + 一句话论断]        [局限/争议]

       [机制 1]  ->  [机制 2]  ->  [机制 3]

       [例子/应用]      [复习问题]      [文件链接]
```

Recommended node sizes:

- center: 560×260
- main concept/mechanism cards: 460×260
- file/review cards: 360×190

## cards.canvas Layout

Cards should be a grid, not a mind map.

- 3 columns by default
- 620×420 per concept card
- 120 px horizontal gap, 120 px vertical gap
- use larger 720×520 cards for formula-heavy or text-heavy concepts
- include all concept cards from the source
- split a long concept into multiple cards instead of overflowing

Card text should be concise and Obsidian-friendly:

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
[[...]] · [[...]]

## 置信度
extracted
```

Use `kind` or `color` metadata when building cards with the helper:

```json
{"title":"彗差", "kind":"risk", "definition":"..."}
{"title":"净灵敏度", "kind":"formula", "latex":"S_{lens} \\propto \\phi_1^2 + k\\phi_2^2"}
{"title":"天平类比", "kind":"example", "intuition":"..."}
```

## formulas.canvas Layout

Formula cards should be a grid. Use blue/cyan labels. For long formulas, increase node width to 680-760 and height to 460-560.

Each card:

```markdown
# 公式卡：公式名 / Original Term

$$
...
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
```

## File Link Nodes

File nodes may link to:

- map.html
- blackboard/01-*.html
- cards.canvas
- formulas.canvas
- ingest-ready.md
- commands.md

Place file links at the bottom or right edge so they do not dominate the learning board.


## V0.2.3 Card Color and Formula Rules

For `cards.canvas`, visually match the blackboard boards:

- Assign mixed Obsidian colors intentionally; never allow all cards to default to green.
- Formula cards or concept cards with prominent formulas should be blue.
- Contradictions, traps, and core problems should be red.
- Examples, analogies, and memory anchors should be yellow.
- Limits, uncertainty, and caveats should be purple.
- Mechanisms and general concepts should be green.

Formula text must use Obsidian math syntax and enough canvas card height:

```markdown
$$
S_{lens} \propto \phi_1^2 + k\phi_2^2
$$
```

If a card contains a formula and more than 4 sections, split it into two cards: one blue formula card and one green/yellow intuition card.
