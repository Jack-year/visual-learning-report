# Visual Learning Report Package Specification

## Folder naming

Use `YYYY-MM-DD--slug`. The slug should be concise, lowercase when possible, and filesystem-safe. Chinese titles are acceptable if the user's vault already uses Chinese names.

## Recommended reading order

1. `README.md`
2. `visual.html`
3. `visual.canvas`
4. `diagrams.md`
5. `formulas.md`
6. `cards.md`
7. `ingest-ready.md`
8. `commands.md`

## Learning depth levels

### Level 1: one-page overview

Answer:

- 这篇材料在解决什么问题？
- 它的核心结论是什么？
- 为什么值得学？
- 读者应该先抓住哪三到五个节点？

### Level 2: layered explanation

Use:

- 背景
- 核心概念
- 论证链
- 例子/应用
- 局限/争议
- 记忆锚点

### Level 3: knowledge extraction

Extract:

- concepts
- entities
- formulas
- claims
- questions
- suggested wikilinks
- confidence labels: `extracted`, `inferred`, `ambiguous`

## Concept card template

```markdown
## 概念卡：<中文名> / <original term>

- 定义：一句话定义。
- 直觉：用类比解释。
- 例子：从原文或常识中取一个例子，标注是否 inferred。
- 容易混淆：说明边界。
- 相关概念：[[...]]
- 置信度：extracted | inferred | ambiguous
```

## Claim extraction template

```markdown
- <claim> [extracted: source section]
- <claim> [inferred]
- <claim> [ambiguous: reason]
```
