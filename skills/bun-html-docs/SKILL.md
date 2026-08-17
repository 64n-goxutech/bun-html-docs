---
name: bun-html-docs
description: Create or substantially update self-contained, beginner-first HTML technical documentation using a reusable Bun-inspired shell with full-text search, generated navigation, contextual Wiki cards, code copy, responsive layout, accessibility, and source-evidence standards. Invoke explicitly as $bun-html-docs for architecture guides, implementation explanations, call-chain documents, debugging guides, change proposals, migrations, or other technical reading pages that must teach an absolute newcomer before introducing implementation terminology and work locally without a server or external assets.
---

# Bun-style HTML Technical Documentation

Create a directly browsable technical document from verified evidence. Reuse the bundled shell so most effort goes into research and explanation rather than rebuilding search, navigation, Wiki, copy, and responsive behavior.

## Establish scope

1. Read and obey the active workspace's `AGENTS.md` and other applicable local instructions.
2. Read [references/content-contract.md](references/content-contract.md) before outlining content.
3. Read [references/shell-authoring.md](references/shell-authoring.md) before creating a new page or updating a page that declares `data-doc-shell="1"`.
4. Resolve the source material, primary reader, topic, and output destination from the request and workspace rules. If no destination is specified, prefer an existing documentation directory; otherwise use `docs/<topic-slug>/` under the active workspace.
5. Treat source material as read-only unless the user separately requests source changes. Keep documentation edits scoped to the selected output directory.

## Follow the workflow

### 1. Classify before outlining

Classify the page as either:

- **Source-understanding document**: explain current implementation, behavior, architecture, or call chains.
- **Change document**: describe a feature, refactor, API adjustment, migration, optimization, or defect fix that would change one or more systems.

For a change document, include `预计改动与影响评估` in the initial outline. Never present proposed behavior as an existing fact.

### 2. Build an evidence map

- Inspect real entries, callers, callees, data structures, tests, configuration, storage, queues, caches, rendering boundaries, and failure paths relevant to the topic.
- Trace across repositories or services when the request crosses a boundary. Do not infer behavior from names alone.
- Prefer executable source and tests over comments or old documents when they disagree.
- Record repository-relative paths and exact symbols for the source map.
- Distinguish `当前事实`, `预计改动`, `合理推断`, and `待确认项` wherever readers could confuse their status.

### 3. Pass the beginner-first opening gate

Draft the opening before the detailed outline. Assume the reader knows neither the repository nor the domain.

- Use a literal reader question, visible symptom, or familiar task for the `h1`; do not stack internal nouns into the title.
- In the lead, state what the reader observes, why it happens in ordinary language, and what the system changes. Keep source symbols and implementation labels out.
- Make the first section a plain-language map such as `what you see → why → what changes → how it stays bounded`.
- Do not use unexplained acronyms, English implementation labels, function names, type names, or repository shorthand in the title, lead, fact line, or first section. A Wiki card does not excuse an opaque opening.
- Introduce every necessary term in this order: plain concept first, project term second, exact source symbol third. Example: “短时间记住最近用过的画面（近期淘汰缓存，源码类型 `ExactVideoFrameCache`）”.
- Keep code, path inventories, module maps, protocol fields, and performance abbreviations below the initial explanation.

The opening passes only if a newcomer can answer: “What problem is this about?”, “Why does it happen?”, and “What are the two or three main ideas?” without opening a Wiki card or reading code.

### 4. Build a progressive explanation

Create a content outline and contextual glossary before authoring. Lead the reader through:

1. a plain-language problem, observable symptom, and two or three core ideas;
2. essential background explained with familiar actions or a restrained analogy;
3. project terminology paired with its plain-language meaning;
4. the global module or service relationship;
5. one verified input-to-output main path;
6. evidence, exact symbols, and ownership boundaries;
7. failures, edge cases, performance effects, and misconceptions;
8. one complete example and a recommended source-reading order.

Write each technical section in two layers: first explain what happens and why in ordinary language, then give the project term and source evidence. Use diagrams only when relationships, state, or sequencing become materially clearer. Keep excerpts short and explain why each one matters.

### 5. Reuse the document shell

- For a new page, run `scripts/scaffold_document.py` into a new topic directory. Edit the generated `index.html`; preserve the content-driven contracts in `styles.css` and `app.js`.
- For an existing shell page, update content without duplicating navigation, search indexes, Wiki definitions, or copy logic.
- For a pre-shell page, inspect its current behavior before deciding whether migration is required. Never overwrite it with the scaffolder.
- Prefer native HTML, CSS, and JavaScript with no network dependency. Keep the document readable when JavaScript is unavailable.
- Keep an explicit `← 文档首页` link visible in the top bar at every viewport and repeat it at the top of the desktop sidebar. Resolve the target relative to the documentation root so it works under direct `file://` access and static hosting such as GitHub Pages.
- Extend the shell only for topic-specific explanatory needs. Do not fork stable search, navigation, Wiki, copy, or mobile behavior without evidence that the shared implementation is insufficient.

### 6. Verify the result

- Open the local HTML file directly with the browser automation tool required by the active workspace. Do not start a preview server solely for verification.
- Verify at `1440 x 900` and `390 x 844`.
- Confirm no page-level horizontal overflow and that tables and code scroll inside their own containers.
- Exercise search success, empty results, ArrowUp, ArrowDown, Enter, Escape, anchor offsets, active navigation, mobile navigation, copy controls, Wiki hover/focus/click, and visible keyboard focus.
- Click the top-bar and sidebar home links from the deepest relevant output path and confirm both reach the documentation root `index.html`.
- Inspect screenshots for clipping, overlap, weak hierarchy, decoration dominating the first viewport, or an opening dominated by unexplained jargon.
- Read only the `h1`, lead, fact line, and first section as a zero-knowledge reader. Rewrite them if understanding depends on source symbols, acronyms, English labels, or later sections.
- Recheck paths, symbols, excerpts, claims, and status labels against their evidence.

## Preserve these invariants

- Deliver HTML rather than substituting Markdown.
- Keep the visual language dense, restrained, and documentation-first rather than landing-page-like.
- Do not rely on external fonts, scripts, styles, images, or network access for core reading behavior.
- Do not start a local server when direct file access satisfies the document.
- Do not modify source systems unless the user explicitly requests those changes.
- Do not claim completion while required interactions or viewport checks remain unverified.
