# FINAL BOOK MASTER — PERMANENT EXECUTION LOCK 0001→2000 (supreme — supersedes all earlier rule files where conflicting)

Source: `CLAUDE_BOOK_MASTER_2000_LESSONS_FINAL_LOCKED_16P_36_38.xlsx`. This
workbook is the single curriculum/master, replacing conflicting older
page/batch/delivery rules from `PROJECT_RULES_ZERO_DEFECT.md` and
`PROJECT_RULES_ABSOLUTE_MASTER.md`. Everything in those files about
per-Lesson content quality (pre-writing gate, exact-objective gate,
English/Vietnamese tests, character lock, duplication control) still
holds — **what changes here is the delivery/batching model.**

## What's new: batch delivery, not per-Lesson delivery
The earlier "one Lesson = one delivery, stop after every Lesson" model is
replaced:

- **A0/Pre-A1 (0001–0250)**: default **37 Lessons per delivery file**.
  Continue writing complete Lessons in exact master order; the **actual
  rendered bilingual page count is the final authority** — adjust the
  number of complete Lessons in the batch (never split a Lesson, never pad,
  never delete valid content) so the delivery finishes at **36–38 actual
  bilingual A4 pages**. English-only page count is *not* hard-locked at
  this level — quality/exact-objective comes first.
- **A1 (0251–0600)**: default **12 Lessons per delivery file**, same
  render-then-adjust logic, same 36–38 actual bilingual page target.
- **A2–B2 (0601–2000)**: **hard content lock** — every single Lesson must
  contain **exactly 16 full A4 pages of English learning content only**
  (Vietnamese, titles, headers, footers, page numbers, blank space, and
  design elements never count toward those 16 pages). Delivery is **ONE
  Lesson = ONE file**: produce full communicative content → verify 16
  English-only pages → add contextual Vietnamese → render → target 36–38
  actual bilingual pages → Final QC → export → stop → wait for `NEXT`.
  16 pages must come from genuine communicative depth (follow-up,
  clarification, repair, reasons, alternatives, disagreement, negotiation,
  compromise, problem solving — only where appropriate to the exact
  Lesson and CEFR level), never repetition or template substitution.

## Audit-then-preserve, not rewrite-on-update
A new master workbook does not by itself invalidate already-approved
Lessons. On receiving an updated master: audit existing Lessons against
it; if a Lesson genuinely passes, **preserve it unchanged** — do not
rewrite correct approved content merely because the master was updated.
Only correct a Lesson if a genuine error is found (and then only the
affected content). Confirmed for this update: Lessons 0001–0007's master
row data (Domain, Scenario, Title, Characters) is byte-identical between
the old and new workbook — no rewrite was needed, and none was made.

## Structural note on hitting the page target
Every Lesson already starts on its own forced page break
(`build_restart_docx.py` calls a new Word section before each Lesson
except the first). Since each A0/Pre-A1 Lesson's actual content
comfortably fits under one page at the book's typography (11pt, 1.3
line-spacing — confirmed by direct measurement: max ~58% of a page used
across Lessons 0001–0037), **Lesson count and actual page count are equal
by construction** at this level. This is why the default "37 Lessons" and
target "36–38 pages" line up almost exactly — no additional padding or
adjustment was needed to hit the range for Batch 1.

## Everything else (unchanged, still in force)
- Master authority: `source_reference/MASTER_2000_LESSONS.csv`
  (`02_MASTER_2000_LESSONS`, now 16 columns including the new page/batch
  fields). Never skip/merge/renumber Lessons or reuse DGE001–401.
- Level lock: 0001–0250 Pre-A1 · 0251–0600 A1 · 0601–1000 A2 · 1001–1400
  B1 · 1401–1700 B1+ · 1701–2000 B2.
- Pre-writing gate, one-Lesson-one-primary-ability, exact-objective
  4-question gate, "topic word ≠ communication skill", Pre-A1 scenario-
  complexity gate — all from `PROJECT_RULES_ZERO_DEFECT.md`, unchanged.
- Two-speaker lock (Ms Lan + one named Mr/Ms), full-form English tested
  for naturalness, Vietnamese translated for meaning/context/relationship
  (never word-for-word, hide-the-English native test, pronouns chosen by
  relationship not defaulted), inline print format, no images/vocab-lists/
  grammar-lectures, zero-padding lock with the explicit high-frequency-
  expression exception — all unchanged.
- QC must be real, never self-declared; delivery gate never sends a known
  FAIL; stop-and-wait-for-NEXT after each delivery (now: after each
  *batch* delivery, not each Lesson, for A0/A1).

## Every-delivery report (exact fields, this workbook's own template)
Lesson range; number of Lessons; CEFR; total English learning words;
English-only A4 pages (A2–B2: 16/Lesson; A0/A1: report actual, not hard-
locked); actual bilingual rendered A4 pages (36–38/file); then PASS/0 for:
exact communication goal, CEFR, English spelling/grammar/syntax/
collocation/register/naturalness, contextual Vietnamese, Vietnamese
pronouns, word-for-word translation errors, meaning loss, unjustified
meaning addition, turn-to-turn logic, exact duplicate English sentences,
artificial near-duplicate padding, cross-Lesson artificial duplication,
images, vocabulary lists, grammar lectures, blank pages, publication
layout; then FINAL QC: PASS.
