---
name: quiz-me
description: Use when the user asks to be quizzed, tested, drilled, or asks Claude to check their understanding of a course topic — e.g. "quiz me on lecture 5", "test me on eigenvalues", "drill me before the midterm".
---

# Quiz Me

Runs a diagnostic-first study session: check what's understood before re-teaching gaps, using the
actual filed notes as ground truth (not general knowledge of the topic).

## Step-by-step

1. **Identify scope.** If the user names a lecture/unit/topic, use that. If they just say "quiz
   me" for a course, pull from everything filed under that course, weighted toward the most
   recently filed material unless told otherwise.
2. **Read the actual filed notes** for that scope (`courses/{slug}/...`) — questions must be
   grounded in what was actually taught (this professor's notation, this problem set's specific
   framing), not a generic textbook version of the topic.
3. **Ask one question at a time.** Mix question types across the session:
   - Recall ("state the theorem")
   - Application (a small problem to work through)
   - Connection ("how does this relate to [prior concept already filed]?")
4. **Wait for the answer before giving feedback.** Don't reveal the answer or move on until the
   user responds.
5. **After each answer:**
   - If correct: confirm briefly, note *why* it's correct in one sentence, move to the next
     question. Don't over-explain something already understood.
   - If incorrect or partial: give the full, step-by-step, fully detailed explanation of the
     concept (per root `CLAUDE.md`'s teaching rules) — walk through the underlying
     workflow/derivation, don't just state the corrected answer. Use LaTeX for any math.
6. **Track weak spots during the session** (mentally, not necessarily written down) and, at the
   end, summarize which specific concepts need more review — this becomes a natural candidate list
   for the `build-cheat-sheet` skill.
7. **Keep sessions bounded** — default to 5–8 questions unless the user asks for more or fewer, so
   a session is useful for a study break rather than an open-ended exam.

## Notes

- This is a quick diagnostic check, not a long multi-round Socratic dialogue — one clarifying
  question per concept before explaining is the pattern from root `CLAUDE.md`, and the same
  restraint applies here: probe once, then teach fully.
- If the user gets a question wrong on a concept that a *later* filed note depends on, flag that
  dependency so they know what to revisit first.
