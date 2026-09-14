---
name: clean-lecture
description: Use when the user asks to clean up, tidy, fix or correct their lecture notes — e.g. "clean up today's lecture", "fix the latex in my notes", "I missed some things in lecture 3, can you fill them in". Reconciles a hand-written lecture note against the slides and the course's reference material.
---

# Clean Lecture

Takes a lecture note typed live during class — with the gaps, typos and broken LaTeX that come
from writing at speaking speed — and reconciles it against the slides for that lecture and the
course's filed reference material.

## The rule that matters most

**The notes are the student's record of what the professor said. The slides are not the truth.**

A professor corrects slides out loud, works examples differently, skips things, and adds things.
So when the note and the source disagree, that is **not** automatically an error in the note.
Three different things can be happening, and they must be handled differently:

| Situation | Action |
|---|---|
| The note is **malformed** (broken LaTeX, typo, `0(n)` for `O(n)`) | Fix it silently |
| The note has a **gap** the source fills | Add it, **marked as added** |
| The note **disagrees** with the source | **Flag it. Do not silently rewrite.** |

Silently "correcting" a note into agreement with the slides destroys the one thing that makes it
worth keeping — the record of what actually happened in the room. It also hides the student's own
misunderstandings, which are exactly what needs to be found before an exam.

## Step-by-step

### 1. Find the note

The argument may be a date, a course slug, both, a path, or nothing at all (meaning **today**).
Search `courses/*/lectures/` and match on, in order: frontmatter `date:`, the date in the
filename, and the date written in the note's first heading. Notes written live often have not been
filed yet, so **expect names like `lec3.md` with no frontmatter** — match on content, not just the
filename pattern.

If several match, list them and ask which. If none match, say so and list the most recent lecture
notes for that course rather than guessing.

### 2. Gather the sources, in this order

1. **Slides or handout for that lecture** — filed beside the note under the same basename
   (`2026-09-15-lecture03-eigenvalues.pdf`), or another file in the same `lectures/` folder
   carrying the same date.
2. **Anything still in `inbox/`** from that date — the slides may have been dumped there and not
   filed yet. File it first with the `file-notes` skill, then use it.
3. **The course's `references/`** — filed textbook chapters. For a course with no slides this is
   the main source; match by topic, not by date.
4. **Earlier notes in the same course**, for continuity of notation and to link back to
   prerequisites.

Convert any PDF that is not already Markdown with
`.claude/skills/file-notes/pdf_to_md.py`. **If no source material exists at all, say so and stop**
— do a LaTeX-and-typo pass only, and be explicit that nothing was checked for correctness. Never
fill gaps from your own knowledge while implying they came from the lecture.

### 3. Snapshot before touching anything

If the note has uncommitted changes, **commit it as-is first**:

```
cmpe-365: lecture 3 notes as taken
```

Then the cleanup is a separate commit and `git diff HEAD~1` shows exactly what changed. Without
this there is nothing to revert to, because a note written today has never been committed.

### 4. Tier 1 — mechanical fixes, applied silently

These cannot be wrong, so just do them:

- **LaTeX correctness**
  - `\theta` → `\Theta` where asymptotic notation is meant (lowercase $\theta$ is an angle;
    $\Theta$ is the tight bound). Same for `\omega` vs `\Omega`.
  - `0(n)` → `O(n)` — digit zero typed for the letter.
  - Unicode `≤ ≥ ≠ ∈ ∞` inside math → `\le \ge \ne \in \infty`.
  - Spacing hacks: `there \ exist \ constants` → `\text{there exist constants}`.
  - Unbalanced delimiters; set-builder written with parens → `\{\, f(n) : \dots \,\}`.
  - Ambiguous fractions: `1/2n^2` → `\tfrac{1}{2}n^2` or `n^2/2`, whichever the note means.
  - Words inside `$$…$$` → `\text{}`, or move them out of math mode entirely.
  - Subscript consistency (`N_0` vs `n_0`).
- **Prose**: spelling ("Symptotic" → "Asymptotic"), `s,t,` → `s.t.`, sentence fragments left
  mid-thought.
- **Structure**: heading hierarchy, list indentation, stray indentation that turns a list into a
  code block.
- **Frontmatter**: add the schema from the root `CLAUDE.md` if missing, with specific tags.
- **Filename**: rename to `YYYY-MM-DD-lectureNN-short-topic.md` with `git mv`.

### 5. Tier 2 — gaps, added and marked

Where the lecture note trails off or skips something the source covers, add it — and **mark it**,
so a later reading can tell what was heard in class from what was reconstructed afterwards:

```markdown
> **[added from CLRS §3.2]** $\Omega(g(n)) = \{\, f(n) : \exists\, c, n_0 > 0 \text{ s.t. }
> 0 \le c\,g(n) \le f(n) \ \forall n \ge n_0 \,\}$
```

An empty section heading with nothing under it is the clearest signal of this — the lecture moved
on before the note caught up.

#### A short section is a request for the full definition, not a small patch

**Note length does not track how important a topic is — it tracks how fast the professor was
talking.** A section that is one line, a fragment, or a bare heading almost always means "I had no
time to write this down", not "this barely came up". Treat it as a placeholder to be filled
properly.

So wherever a section is a stub, **write out the complete formal mathematical definition**, in
proper LaTeX, to the same standard as the sections that did get written out in full. Include:

- the **formal statement** — set-builder form, all quantifiers, all constants, the conditions they
  must satisfy, and the range of $n$ over which the condition holds;
- the **plain-language reading** of what it means, one sentence;
- a **worked example** if the neighbouring sections have them, so the section matches the rest of
  the note;
- how it **relates to the definitions around it** (e.g. that $\Theta$ is exactly $O$ and $\Omega$
  together).

Do not write a one-line summary and move on. An under-filled section is the failure mode here: the
whole reason to flag it is that there is nothing there to revise from.

**Worked example — the real one from `cmpe-365` lecture 3.** The note ends with a bare heading:

```markdown
### Symptotic notation (omega) $\Omega$
```

That is not "omega was skipped in the lecture"; it is "the lecture reached omega and the typing did
not." The section should come out as a full definition, marked as added:

```markdown
### Asymptotic notation (omega) $\Omega$

> **[added from CLRS §3.2 — the lecture note stopped at the heading]**

$\Omega$ gives an **asymptotic lower bound**: $f(n)$ grows at least as fast as $g(n)$, to within a
constant factor.

$$\Omega(g(n)) = \{\, f(n) : \exists\ c > 0,\ n_0 > 0 \ \text{ s.t. } \ 0 \le c\,g(n) \le f(n)
\ \text{ for all } n \ge n_0 \,\}$$

Mirror image of $O$: where $O$ caps $f(n)$ above by $c\,g(n)$, $\Omega$ floors it below. And the
three fit together as

$$f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \ \text{ and } \ f(n) = \Omega(g(n))$$

which is the formal version of the line already in the note, "theta has both upper and lower
bounds, big O has just upper bound".
```

Where the definition comes from matters. Take it from the course's own sources — the slides for
that lecture, or the filed textbook — so the notation matches what the professor uses. If **no**
source is available, a standard definition may still be added, but say so in the marker
(`> **[added — standard definition, not from your course sources; check the notation matches]**`)
rather than implying it came from the lecture.

### 6. Tier 3 — disagreements, flagged and never silently rewritten

When the note states something the source contradicts, leave the note's wording in place and add
the flag next to it:

```markdown
> ⚠️ **Check this.** Your note says $f(n)$ is bounded by $c_1 f(n)$ and $c_2 f(n)$; CLRS §3.2
> bounds it by $c_1 g(n)$ and $c_2 g(n)$. Bounding $f$ by itself is trivially true, so this is
> probably a slip — but if the professor wrote it this way, keep your version and tell me.
```

Say **which** source disagrees and **why it matters**. Distinguish two cases explicitly:

- **A real error** — the definition is incomplete, a bound is inverted, a symbol is wrong. Say so
  plainly and give the correct statement.
- **A legitimate variation** — a different $n_0$, a different constant, a different but valid
  derivation path. **This is not an error.** Do not "fix" it toward the textbook; note that the
  professor's working differs and move on.

### 7. Teach the gap, don't just patch it

Per the root `CLAUDE.md`, an explanation comes with the correction. When a Tier 3 flag is a real
misunderstanding, add a short explanation of *why* — one or two sentences, in LaTeX, linked back
to earlier filed material. A patched note the student doesn't understand fails the purpose of
this repo.

### 8. Report

State plainly:

- `old path → new path` if renamed.
- **Tier 1**: a count and the categories ("11 LaTeX fixes: 6 × `\theta`→`\Theta`, 2 unbalanced
  delimiters, …"). Don't list every one.
- **Tier 2**: each addition, one line, with its source.
- **Tier 3**: each flag, in full — these need the student's attention and are the real output.
- **What had no source to check against**, explicitly.

Then update the course's `CLAUDE.md` "covered so far", and add anything the student got wrong to
"known trouble spots" so `quiz-me` and `build-cheat-sheet` target it later.

## Notes

- Never delete something the student wrote. Rephrasing for grammar is fine; removing a claim is
  not — flag it instead.
- If the note is already clean, say so. Don't manufacture changes to look useful.
- Keep the student's voice. This is their revision material, not a textbook rewrite: if they wrote
  "theta has both upper and lower bounds, big O has just upper bound", that is a good note. Fix
  the capitalisation and leave the sentence alone.
