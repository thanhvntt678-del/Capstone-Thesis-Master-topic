# PERMANENT ZERO-DEFECT PRODUCTION LOCK (supreme — supersedes all earlier rule files where conflicting)

This file is the verbatim-substance, permanent production command for
**EVERYDAY ENGLISH REFLEX BOOK, Lesson 0001 → 2000**, replacing
`PROJECT_RULES_ABSOLUTE_MASTER.md` wherever they conflict. Applies
automatically to every future `NEXT` without restatement. The curriculum
data in `source_reference/MASTER_2000_LESSONS.csv` remains the sequence
authority regardless of rule-file changes.

## What's genuinely new here (the reason this file exists)
Everything from `PROJECT_RULES_ABSOLUTE_MASTER.md` still holds (master
authority, level lock, source hierarchy, reference-first workflow, Pre-A1
lock, English/Vietnamese quality tests, duplication control, editorial
targets, publication design, cumulative book, stop lock, QC report shape).
**Three additions sharpen it, and were immediately applied retroactively
to Lesson 0003 in this same turn:**

1. **ONE LESSON = ONE PRIMARY COMMUNICATIVE ABILITY (absolute).** State
   internally, before writing: "what is the ONE primary communicative
   ability this Lesson develops?" (from Title + Scenario + Goal). Every
   turn must serve only that ability, or a necessary/appropriate/
   non-future-leaking support role.

2. **Exact-Objective Gate, per turn, four questions:**
   A) Is this turn necessary/genuinely useful for THIS Lesson's exact
      goal? B) Is its function appropriate to THIS CEFR level? C) Does it
      accidentally teach a skill that belongs to a later Lesson? D) Does
      it make the scenario more complex than necessary? Insert only if
      A=YES, B=YES, C=NO, D=NO.

3. **Topic word ≠ communication skill.** A target word appearing (e.g.
   "numbers") does not license a more complex scenario just because that
   word could plausibly appear there. Concretely: numbers 0–20 does not
   license multi-step requests, arithmetic/combining numbers, a second
   "extended" quantity question, or problem-solving framing (a missing/
   lost object) — none of that is required by "recognise and respond to
   a number," and all of it was present in the first draft of Lesson
   0003 (asking for help counting misplaced keys, then asking about a
   *second* box, then "Nine and six" combining the two). Caught by this
   gate and rewritten to a single clean number exchange (How many apples
   are there? / There are seven apples. / Seven apples, thank you. / You
   are welcome. — 4 turns, 16 words) before Lesson 0004 was started.

4. **Pre-A1 scenario-complexity gate, checked separately from language
   level.** Simple vocabulary inside a complex situation still FAILs.
   Both language level AND scenario complexity must independently read
   as Pre-A1-appropriate.

## Everything else, condensed (full detail already in PROJECT_RULES_ABSOLUTE_MASTER.md)
- Master authority: `02_MASTER_2000_LESSONS` / `source_reference/MASTER_2000_LESSONS.csv`.
  Never skip/merge/renumber Lessons, invent curriculum, or reuse DGE001–401.
- Level lock: 0001–0250 Pre-A1 · 0251–0600 A1 · 0601–1000 A2 · 1001–1400 B1
  · 1401–1700 B1+ · 1701–2000 B2. "A0" = reader label only, CEFR-valid name
  is Pre-A1.
- Source hierarchy: CEFR Companion Volume (level authority) > Cambridge
  Pre A1 Starters (simplicity calibration only, never content/characters/
  exam material) > Cambridge Dictionary (English validation) > Cambridge
  EN–VI (meaning cross-check only, never final translation). `coe.int`,
  `cambridgeenglish.org`, `dictionary.cambridge.org` are blocked by this
  sandbox's egress proxy — trained knowledge substitutes.
- Reference-first, never write-then-fix: MASTER → reference check → CEFR
  check → exact-objective check → scenario-complexity check → turn-
  function plan → English pre-validation → Vietnamese translation plan →
  write → self-QC → render → Final QC → export.
- Setting ≠ objective (a clinic/shop/street setting never expands what
  gets taught).
- Two-speaker lock: Ms Lan + exactly one named Mr/Ms secondary character,
  never Person A/B.
- English: full-form preferred but must stay natural (rewrite the whole
  sentence rather than force an awkward full form); native-naturalness
  test before insertion, not at final QC.
- Vietnamese: never word-for-word; pipeline meaning→intention→situation→
  relationship→tone→politeness→natural Vietnamese; hide-the-English native
  test; pronouns chosen from relationship/context, never a tôi/bạn
  default, consistent within a Lesson.
- Duplication: zero exact/near-duplicate padding, zero artificial cross-
  Lesson duplication — but natural high-frequency expressions (Hello,
  Good morning, Thank you, Goodbye, You are welcome) may legitimately
  recur; don't distort natural English to avoid them.
- Word/page targets are editorial only. Priority order, absolute: 1 CEFR
  accuracy 2 exact communication goal 3 scenario appropriateness 4 natural
  English 5 natural contextual Vietnamese 6 real communicative value 7
  dialogue logic 8 no artificial duplication 9 word/page target. Accept a
  shorter Lesson rather than pad.
- Publication: consistent A4 navy/light-blue professional design, zero
  images/vocab-lists/grammar-lectures, zero blank/near-blank pages, zero
  page-count manipulation.
- Cumulative book always contains every approved Lesson 0001→N in order
  (already satisfied structurally — `build_restart_docx.py` globs and
  renders every `lesson_*.json` in sorted order each run).
- Don't rewrite an already-approved Lesson without a genuine
  language/translation/CEFR/duplication/continuity error.
- QC must be real, never self-declared without actual inspection.
- Stop lock: export → report → STOP after one Lesson; never auto-start
  the next; wait for `NEXT`.
- After Lesson 2000: whole-book audit (missing IDs, order, CEFR
  progression, curriculum coverage, duplication, English/Vietnamese
  quality, pronoun consistency, layout/page-number continuity, blank
  pages, publication integrity) — correct only genuine problems.

## Final QC report — exact fields (per this command's own template)
`LESSON [XXXX] — FINAL QC REPORT`: Lesson ID, CEFR, Major Domain,
Scenario, English Title, Vietnamese Title, Primary Communication Goal,
Master Row, CEFR, Exact Objective, Scenario Complexity, Main Character
(Ms Lan — PASS), Secondary Character (Mr/Ms [Name] — PASS), Active
Speakers (2 — PASS), English Spelling/Grammar/Syntax/Collocation/
Register/Politeness/Naturalness, Contextual Vietnamese, Natural
Vietnamese, Pronoun Consistency, Word-for-word Translation Errors,
English-shaped Vietnamese, Meaning Loss, Unjustified Meaning Addition,
Turn-to-turn Logic, Real-life Communication, Exact Duplicate Sentences,
Artificial Padding, Cross-Lesson Artificial Duplication, Images, Image
Placeholders, Vocabulary Lists, Standalone Grammar Lectures, Blank Pages,
Near-Blank Pages, English Learning Words, Actual Bilingual A4 Pages,
Publication Layout, FINAL QC, STATUS (`LESSON [XXXX] COMPLETE — WAITING
FOR NEXT`).
