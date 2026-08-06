# bun-html-docs

一个用于生成和维护 Bun 风格 HTML 技术文档的 Codex Skill。

它把稳定的文档框架、视觉规范和交互能力封装为可复用资源，让 Codex 将主要精力放在源码研究、调用链梳理和内容表达上，而不是在每个任务中重新实现搜索、目录、Wiki 和响应式布局。

## 能力

- Bun 风格的高密度技术文档布局
- 原生 HTML、CSS 和 JavaScript，无构建依赖
- 全文搜索、匹配摘要、空结果和键盘导航
- 根据正文自动生成章节目录和当前章节高亮
- 支持悬停、键盘聚焦和移动端点击的术语 Wiki 卡
- 自动增强的代码复制按钮
- 桌面与移动端响应式布局
- 代码块和表格容器内横向滚动
- 语义化 HTML、可见焦点和基础无障碍支持
- 面向源码理解文档和变更型文档的内容规范
- 可离线直接打开，不依赖外部字体、脚本或样式

## 安装

仓库推送到 GitHub 后，可以使用 Codex 自带的 Skill 安装脚本：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <github-owner>/bun-html-docs \
  --path skills/bun-html-docs
```

也可以克隆仓库后，将 `skills/bun-html-docs` 复制到个人 Skill 目录：

```text
~/.codex/skills/bun-html-docs
```

安装后，从下一个 Codex 任务开始可用。

## 使用

显式调用 Skill：

```text
使用 $bun-html-docs，研究当前项目的任务调度链路，并生成一篇面向新读者的 HTML 技术文档。
```

变更型文档示例：

```text
使用 $bun-html-docs，为缓存失效机制重构生成 HTML 方案文档，包含预计改动与影响评估。
```

Skill 会优先遵守当前工作区的 `AGENTS.md`。源码位置、输出目录和项目专用规则应由当前工作区或用户请求提供，不写死在这个通用 Skill 中。

## 文档脚手架

安装后可以直接生成一个新的文档目录：

```bash
python3 ~/.codex/skills/bun-html-docs/scripts/scaffold_document.py \
  --output /absolute/path/to/docs/topic-slug \
  --title "Document title" \
  --summary "One sentence explaining the problem and system position" \
  --label "ARCHITECTURE · SOURCE GUIDE"
```

输出内容：

```text
topic-slug/
├── index.html
├── styles.css
└── app.js
```

脚手架不会覆盖已有的同名文件。生成后主要编辑 `index.html`；目录、搜索索引、Wiki 卡片和代码复制会从 HTML 内容自动派生。

## 内容原则

每篇文档应帮助不了解项目的读者建立正确心智模型，并沿一条有证据的主链路理解输入、处理、状态变化、输出和失败路径。

文档需要区分：

- `当前事实`：由当前源码、测试或权威资料直接支持
- `预计改动`：尚未实现的方案
- `合理推断`：有证据支持但没有明确保证的判断
- `待确认项`：需要用户决策或更多资料才能确定的内容

变更型文档需要独立的“预计改动与影响评估”，覆盖范围与非目标、数据结构变化、上下游影响、风险、验证、回退和待确认决策。

## 仓库结构

```text
bun-html-docs/
├── README.md
└── skills/
    └── bun-html-docs/
        ├── SKILL.md
        ├── agents/
        ├── assets/
        ├── references/
        └── scripts/
```

## 隐私边界

这个仓库只保存通用文档能力，不包含项目仓库名称、本机用户名、绝对源码路径或固定输出目录。项目专用映射应保存在对应工作区的 `AGENTS.md`、私有配置或调用提示中。
