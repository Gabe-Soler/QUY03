Clean up a lecture note, reconciling it against that lecture's slides and the course's reference
material: $ARGUMENTS

Run the `clean-lecture` workflow (see `.claude/skills/clean-lecture/SKILL.md`).

The argument above may be a date, a course slug, both, a file path, or empty — **empty means
today's lecture**. If it matches more than one note, list them and ask rather than guessing.

Three rules that govern the whole pass:

1. **Fix what cannot be wrong, silently** — broken LaTeX, `\theta` where `\Theta` is meant,
   `0(n)` for `O(n)`, typos, headings, frontmatter, filename.
2. **Fill gaps from the slides or textbook, and mark them** as added so it stays obvious later
   which parts were heard in the lecture and which were reconstructed after it. A section that is
   one line, a fragment, or a bare heading means the lecture outran the typing — **not** that the
   topic was minor. Fill those with the **complete formal definition** (full set-builder form,
   every quantifier and constant, the range of $n$), plus a plain-language reading and a worked
   example if the neighbouring sections have them. A one-line summary is not enough: there has to
   be something there to revise from.
3. **Never silently rewrite a disagreement.** If the note contradicts the slides, flag it with
   both versions and say which source disagrees — the professor may have corrected the slides out
   loud, or the note may be a mishearing, and only the student knows which.

Commit the note as-is before changing it, so the cleanup is a separate, revertible commit. Report
Tier 1 as counts, and Tier 3 flags in full — those are the part that matters.
