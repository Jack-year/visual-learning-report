# Visual Learning Report

> Claude Code 可视化学习报告生成技能

将困难的文章、PDF 章节、论文、技术文档转化为自包含的学习包，包含黑板风格 HTML 讲解页、Obsidian Canvas 知识图谱、Mermaid 流程图、概念卡片、公式卡片和入库就绪的结构化 Markdown。

## 适用场景

- 学习光学、数学密集型技术材料
- 阅读论文、微信公众号技术文章
- 为 LLM Wiki 知识库生成可审核的素材
- 制作自包含的学习笔记包

## 产出物

| 文件 | 说明 |
|------|------|
| `visual.html` | 🖼️ 黑板风格的可视化教学页（含封面+分层讲解+自测） |
| `visual.canvas` | 🗺️ Obsidian Canvas 知识图谱 |
| `diagrams.md` | 📊 Mermaid 流程图/概念关系图/因果链 |
| `formulas.md` | 📐 公式卡片（LaTeX + 人话解释） |
| `cards.md` | 🃏 概念闪卡 |
| `ingest-ready.md` | 📄 入库就绪的结构化 Markdown（含置信度标签） |
| `README.md` | 📘 报告包入口与阅读指引 |
| `commands.md` | ⚡ Claude Code 操作命令 |

## 安装

```bash
npx skills install visual-learning-report
```

## 使用

在 Claude Code 中直接调用：

```
对 raw/articles/xxx.md 生成可视化学习报告
```

## 文件结构

```
visual-learning-report/
├── SKILL.md                              # 技能定义
├── references/
│   ├── report-package-spec.md            # 报告包详细模板
│   └── blackboard-html-style.md          # 黑板 HTML 样式指南
├── scripts/
│   └── create_canvas.py                  # Obsidian Canvas 生成脚本
└── agents/
    └── openai.yaml                       # Agent 配置
```
