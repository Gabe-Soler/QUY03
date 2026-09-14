---
name: concept-map
description: Use when the user asks how concepts relate, what the prerequisites for a topic are, or wants a dependency/concept map — e.g. "what do I need to understand before eigendecomposition", "map out how these topics connect", "what does this concept depend on".
---

# Concept Map

Traces prerequisite and dependency relationships between concepts across the filed notes — useful
in a math/engineering program where almost everything builds on something earlier.

## Step-by-step

1. **Identify the target concept** the user is asking about.
2. **Search filed notes across the whole course (or repo, if cross-course)** for:
   - Where the concept is first introduced
   - What earlier concepts it explicitly builds on or references (look for phrases like "recall
     that," "using the result from," or notation reused from earlier lectures)
   - What later concepts depend on it, if any are already filed
3. **Present the result as a short chain, not a full explanation**:
   ```
   Sets → Linear independence → Basis → Eigenvalues → Eigendecomposition → Diagonalization
   ```
   with a one-line note on *why* each link exists (what specifically carries over), not a full
   re-explanation of each concept (that's what direct explanation / `quiz-me` is for).
4. **Flag gaps** — if a dependency the concept clearly relies on hasn't been filed yet (not yet
   covered in lecture, or missed capture), say so explicitly rather than silently skipping it.
5. If the user wants the full explanation of any node in the chain rather than just the map, switch
   to the normal teaching flow from root `CLAUDE.md` (diagnostic question, then full step-by-step
   explanation) for that specific concept.

## Notes

- Keep the map itself short — it's a navigation aid, not a document. If the user wants it saved,
  write it to `courses/{slug}/summaries/` rather than leaving it only in chat.
