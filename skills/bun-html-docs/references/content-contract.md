# Content and experience contract

## Reader outcome

Write for a reader with no prior knowledge. Explain why the topic exists, who owns each responsibility, how components cooperate, how data changes, and what happens when work fails. Avoid turning the page into a directory, type, or function inventory.

## Beginner-first opening contract

The opening is a teaching surface, not an executive summary for people who already know the codebase. Assume the reader does not know the repository, domain abbreviations, internal English labels, or source types.

The first viewport and first section must establish, in this order:

1. **Observable problem:** what the user, operator, or developer actually sees or tries to do.
2. **Plain cause:** why it happens using familiar actions and concrete nouns.
3. **Core ideas:** the two or three changes, responsibilities, or decisions that explain the topic.
4. **Safety boundary:** what prevents the solution from waiting forever, using unlimited memory, corrupting state, or overriding newer work when relevant.

Use a question, visible symptom, or literal task as the title. Write the lead so it makes sense without the rest of the page. A useful first-section structure is:

Titles, navigation labels, and section intros should state the topic, conclusion, or mechanism directly. Avoid slogans that narrate how the reader is expected to read; the document should explain the subject itself.

| What the reader sees | Why it happens | What the system does | How it stays bounded |
| --- | --- | --- | --- |
| Familiar symptom | Plain cause | Plain action | Timeout, limit, cancellation, ownership, or compatibility rule |

Do not put these in the title, lead, fact line, or first section before explaining them:

- acronyms such as GOP, PCM, LRU, RPC, QoS, or ETA;
- implementation labels such as exact, warmup, prime, pending, sibling, owner, or source;
- function, class, type, event, protocol, or repository-internal names;
- compressed phrases that only make sense after reading the source.

When a technical term is necessary, introduce it as `plain meaning → project term → exact symbol`. For example: “短时间记住最近用过的画面（近期淘汰缓存，源码类型 `ExactVideoFrameCache`）”. Do not use a glossary or Wiki popover as a substitute for explaining the first occurrence in the body.

Before accepting the outline, read only the opening and verify that a newcomer can answer:

- What problem is this document about?
- Why does that problem happen?
- What are the two or three main ideas?
- What important limit or failure rule keeps the change safe?

If any answer requires opening a Wiki card, understanding an acronym, or reading source code, rewrite the opening.

Use this narrative order unless the topic clearly needs another:

1. plain-language problem, observable symptom, and core ideas;
2. essential background explained through familiar actions or a restrained analogy;
3. minimal mental model with plain meanings paired to project terminology;
4. global relationship among modules or services;
5. one real end-to-end path from input through state changes to output;
6. source or evidence map with exact relative paths and symbols;
7. failures, boundaries, performance implications, and common misconceptions;
8. a complete example and recommended reading order.

Use two layers inside technical sections: first explain what happens and why in ordinary language; then supply project names, source symbols, formulas, or protocol details. Preserve rigor by moving evidence deeper, not by removing it.

Label facts and uncertainty clearly:

- `当前事实`: directly supported by current source, tests, or authoritative evidence.
- `预计改动`: proposed work that does not exist yet.
- `合理推断`: bounded inference supported by evidence but not guaranteed.
- `待确认项`: a decision or fact the available evidence does not settle.

## Required change section

For a change document, add a standalone `预计改动与影响评估` section containing:

1. objective, affected systems, modules, files or interfaces, scope, and non-goals;
2. ordered additions, modifications, migrations, or deletions, with ownership and rationale;
3. before/after types, APIs, persistence, state, or event protocols, including defaults, lifecycle, and compatibility;
4. callers, callees, shared components, cache, storage, queues, rendering, tools, tests, configuration, and existing-data impact;
5. relevant compatibility, consistency, concurrency, timing, performance, permission, security, recovery, rollout, and migration risks;
6. tests, acceptance scenarios, observability, rollback, and any irreversible step;
7. unresolved decisions and the parts of the plan each decision affects.

Say explicitly when data structures or downstream systems are unchanged and cite boundary evidence. Never infer “no impact” from naming alone.

## Required reading experience

- Full-text search with section, snippet, empty state, ArrowUp/ArrowDown, Enter, and Escape.
- Generated table of contents matching stable anchors, synchronized active state, and header-safe offsets.
- Contextual Wiki definitions available by hover, keyboard focus, and mobile click.
- Evidence map with real sources, relative paths, exact symbols, and ownership.
- Horizontally scrollable code and tables, plus copy controls where useful.
- Responsive layout, semantic HTML, accessible labels, visible focus, and keyboard operation.
- Progressive enhancement: core text remains readable without JavaScript.

## Bun-inspired visual baseline

Use a high-density technical-document layout, not a landing page, dashboard, or card gallery.

```css
:root {
  --page: #0c0a0b;
  --surface: #141113;
  --line: #2a2528;
  --ink: #f4eff1;
  --muted: #b9b1b5;
  --subtle: #8f888c;
  --accent: #ff6da8;
  --accent-soft: #2b1821;
}
```

- Use a 64px compact top bar, 288px desktop sidebar, at most a 1440px shell, and at most a 900px reading column.
- Use 36px desktop and 32px mobile `h1`; 24-28px desktop and 22-24px mobile `h2`; 16px body with 1.6-1.65 line height; 13-14px code.
- Use stable pixel/rem sizes, system fonts, 1px dividers, 6px normal radius, and never exceed 8px radius.
- Use neutral black surfaces and restrained pink emphasis. Avoid gradients, glow, textures, decorative blobs, glass effects, marketing heroes, nested cards, and illustration-first screens.
- Keep sections in continuous reading flow. Use bordered or left-accent callouts only when content warrants them.
- Hide the fixed sidebar on tablet/mobile and provide a compact directory entry. Use 20px mobile padding, reducible to 16px, and at least 36px touch targets.
- Do not use viewport-width font sizing. Keep long paths, identifiers, tables, code, buttons, and fixed elements from creating page-level overflow or overlap.
- Keep interaction feedback restrained and respect `prefers-reduced-motion`.

## Completion checks

Verify `1440 x 900` and `390 x 844`, including page width equality, internal table/code scrolling, search states and keyboard navigation, anchors, active sections, copy, Wiki hover/focus/click, mobile navigation, and visible focus. The first viewport must lead with the topic and content hierarchy rather than decoration.

Also inspect only the title, lead, fact line, and first section. Reject the page if this opening is a symbol inventory, acronym wall, compressed implementation summary, or text that becomes understandable only after later sections.
