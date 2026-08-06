# Content and experience contract

## Reader outcome

Write for a reader with no prior knowledge. Explain why the topic exists, who owns each responsibility, how components cooperate, how data changes, and what happens when work fails. Avoid turning the page into a directory, type, or function inventory.

Use this narrative order unless the topic clearly needs another:

1. one-sentence problem and system position;
2. essential background, terminology, and minimal mental model;
3. global relationship among modules or services;
4. one real end-to-end path from input through state changes to output;
5. source or evidence map with exact relative paths and symbols;
6. failures, boundaries, performance implications, and common misconceptions;
7. a complete example and recommended reading order.

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
