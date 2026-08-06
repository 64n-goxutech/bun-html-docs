---
name: bun-html-docs
description: Create or substantially update self-contained, reader-facing HTML technical documentation using a reusable Bun-inspired documentation shell with full-text search, generated navigation, contextual Wiki cards, code copy, responsive layout, accessibility, and source-evidence standards. Invoke explicitly as $bun-html-docs for architecture guides, implementation explanations, call-chain documents, debugging guides, change proposals, migrations, or other technical reading pages that should work locally without a server or external assets.
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

### 3. Design for a new reader

Create a content outline and contextual glossary before authoring. Lead the reader through:

1. the problem and system position;
2. essential background and a minimal mental model;
3. the global module or service relationship;
4. one verified input-to-output main path;
5. evidence and ownership boundaries;
6. failures, edge cases, performance effects, and misconceptions;
7. one complete example and a recommended source-reading order.

Use diagrams only when relationships, state, or sequencing become materially clearer. Keep excerpts short and explain why each one matters.

### 4. Reuse the document shell

- For a new page, run `scripts/scaffold_document.py` into a new topic directory. Edit the generated `index.html`; preserve the content-driven contracts in `styles.css` and `app.js`.
- For an existing shell page, update content without duplicating navigation, search indexes, Wiki definitions, or copy logic.
- For a pre-shell page, inspect its current behavior before deciding whether migration is required. Never overwrite it with the scaffolder.
- Prefer native HTML, CSS, and JavaScript with no network dependency. Keep the document readable when JavaScript is unavailable.
- Extend the shell only for topic-specific explanatory needs. Do not fork stable search, navigation, Wiki, copy, or mobile behavior without evidence that the shared implementation is insufficient.

### 5. Verify the result

- Open the local HTML file directly with the browser automation tool required by the active workspace. Do not start a preview server solely for verification.
- Verify at `1440 x 900` and `390 x 844`.
- Confirm no page-level horizontal overflow and that tables and code scroll inside their own containers.
- Exercise search success, empty results, ArrowUp, ArrowDown, Enter, Escape, anchor offsets, active navigation, mobile navigation, copy controls, Wiki hover/focus/click, and visible keyboard focus.
- Inspect screenshots for clipping, overlap, weak hierarchy, or decoration dominating the first viewport.
- Recheck paths, symbols, excerpts, claims, and status labels against their evidence.

## Preserve these invariants

- Deliver HTML rather than substituting Markdown.
- Keep the visual language dense, restrained, and documentation-first rather than landing-page-like.
- Do not rely on external fonts, scripts, styles, images, or network access for core reading behavior.
- Do not start a local server when direct file access satisfies the document.
- Do not modify source systems unless the user explicitly requests those changes.
- Do not claim completion while required interactions or viewport checks remain unverified.
