# Reusable document shell

## Scaffold a new page

Run the bundled script from the skill directory:

```bash
python3 scripts/scaffold_document.py \
  --output /absolute/path/to/docs/topic-slug \
  --title "Literal reader question or familiar problem" \
  --summary "Plain-language symptom, cause, and core idea without source terminology" \
  --label "TECHNICAL · SOURCE GUIDE"
```

Optionally pass `--root /absolute/docs/root` to require the output directory to be nested below a known documentation root.

The script creates `index.html`, `styles.css`, and `app.js` and refuses to overwrite any of them. Use it only for a new topic directory.

Treat `--title` and `--summary` as novice-facing copy, not metadata for experts. Do not pass acronym stacks, internal component names, source symbols, or compressed implementation summaries. The scaffold places them in the browser title and first viewport.

## Author content without duplicate UI state

- Add `data-searchable` to every top-level section that belongs in search and navigation.
- Set `data-nav="Short label"` when the heading is too long for the sidebar.
- Set `data-group="Group"` to label search results.
- Give each searchable section a stable kebab-case `id`.
- Keep one `h1` in the introduction and one `h2` in each searchable section.
- Do not maintain a separate table of contents; `app.js` derives it from sections.
- Keep the generated `plain-summary` section first. Replace its placeholders with observable symptoms, ordinary-language causes, core actions, and relevant limits before adding implementation terminology.

The shell indexes section text, navigation labels, groups, and inline code; ranks matches; creates snippets; handles empty results; and supports ArrowUp, ArrowDown, Enter, Escape, `/`, and Command/Ctrl+K.

## Add Wiki terms

Create an inline trigger:

```html
<button class="wiki-term" type="button" data-wiki="runtime">Runtime</button>
```

Add exactly one visible glossary definition:

```html
<article class="glossary-entry" data-wiki-definition data-term="runtime" data-category="Runtime">
  <h3>Runtime</h3>
  <p data-wiki-summary>An object graph that owns resources and state while a system is running.</p>
  <p><strong>In this system:</strong> Add the topic-specific meaning.</p>
</article>
```

The shell derives hover, focus, and click cards from the visible glossary. Do not duplicate definitions in JavaScript. Explain first-use core terms in prose; Wiki cards are for recall.

## Add code and tables

```html
<div class="code-block" data-code-title="Call-chain outline">
  <pre><code>short, verified excerpt</code></pre>
</div>
```

Wrap tables in `<div class="table-wrap">`. Keep paths and symbols in `code`. Prefer prose, sequences, comparison tables, and restrained callouts over card grids.

## Extend safely

- Put topic-only CSS after the base stylesheet or in a clearly marked final section.
- Put substantial topic-only behavior in a separate file; do not fork stable search, Wiki, navigation, or copy logic.
- Preserve `data-doc-shell="1"`. Increment the marker only for an incompatible shell contract.
- Preserve semantic landmarks, labels, focus handling, reduced-motion styles, and no-script readability.
