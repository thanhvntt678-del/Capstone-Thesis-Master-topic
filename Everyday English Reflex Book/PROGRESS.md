# Everyday English Reflex — Production Progress

Master reference: `source/CLAUDE_BOOK_MASTER_2000_LESSONS_FINAL_LOCKED.xlsx`
(sheet `02_MASTER_2000_LESSONS` has the row-by-row Lesson ID / CEFR / domain /
scenario / title / secondary-character spec for all 2000 lessons.)

## Status

- **Last completed lesson: 0006**
- **Next lesson to write on NEXT: 0007** (A0/Pre-A1, domain "Shopping",
  scenario "the first practical exchange about shopping & payments",
  secondary character Mr Thomas)
- Current delivery file: `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0001-0006.docx`
  (Lesson 0001 preserved verbatim from the approved upload + Lessons 0002-0006
  newly written and QC-checked. The 0001-0005 delivery file was superseded by
  this one and removed — always keep exactly ONE current delivery file per
  batch, named for its full lesson range.)
- Structural page estimate for this 6-lesson file: **~31 pages** (English-only
  calibration against the approved Lesson 0001; see "Known environment
  limitation" below — real rendering was not available to confirm). Still
  short of the ~36–38 page A0 combined target. **Interpretation adopted for
  NEXT:** each NEXT adds one more fully QC'd lesson to this same delivery
  file (never a new file, never a partial lesson) and reports updated
  cumulative counts; once the estimate is comfortably inside ~36–38 pages,
  that delivery is closed out and the next NEXT starts a fresh combined file
  beginning at the following lesson.

## Per-lesson QC record (English learning words, excl. Vietnamese)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0001 (approved, preserved) | Personal Identity | Mr David | 829 | 132 | 0 |
| 0002 | Social Basics | Ms Emma | 1018 | 140 | 0 |
| 0003 | Numbers and Time | Mr James | 993 | 141 | 0 |
| 0004 | Home | Ms Sarah | 983 | 139 | 0 |
| 0005 | Family | Mr Daniel | 950 | 143 | 0 |
| 0006 | Food | Ms Olivia | 1007 | 127 | 0 |

Total English learning words, Lessons 0001-0006: **5,780**.

Cross-lesson exact-duplicate English line check now covers **Lesson 0001
too** (`build_combined.py`'s `load_lesson0001_as_dict()` parses the approved
docx into the same shape as every other lesson, and `cross_lesson_duplicate_check()`
runs over `[lesson_0001] + LESSONS_NEW`). This caught 7 real duplicates on
the 0006 build (e.g. "Good morning, Lan!", "It is my pleasure.", "Thank you
very much." each already used in Lesson 0001) that a 0002-0005-only check
had missed — all fixed by rewording the 0002/0004 copies. **Always run the
full `build_combined.py` (not a partial manual check) before calling a
lesson done** — it now catches this automatically. Current result: **0
duplicates across all 6 lessons.**

## Tooling (reusable for every future lesson, A0 through B2)

- `source/lesson_builder.py` — python-docx builder matching the APPROVED
  Lesson 0001 style exactly: A4 page (7560310 x 10692130 EMU), margins
  720090/647700 EMU, Arial title block, navy/light-blue lesson header table,
  italic 9.5pt bilingual intro paragraph, Calibri 11pt dialogue lines
  (bold speaker name, plain English, italic Vietnamese) at 1.3 line spacing,
  footer with page-number field. Also has `qc_report()` /
  `find_exact_duplicate_lines()` / `find_exact_duplicate_sentences()` /
  `lesson_word_count()` helpers — **always run these on a new lesson before
  it is considered done.**
- `source/lessonNNNN.py` — one data file per lesson: a `LESSON_NNNN` dict
  with `lesson_id, cefr, domain, en_title, vi_title, intro_en, intro_vi,
  turns` (list of `(speaker, english, vietnamese)` tuples). This is the
  pattern to follow for every future lesson.
- `source/build_combined.py` — loads `lesson0001_approved.docx` as the base
  (so Lesson 0001 is never regenerated/edited) and appends each new lesson
  with a page break, then rewrites the footer to the combined lesson range.
  Update the `LESSONS_NEW` import list here each time a new lesson is added,
  and rerun before every delivery.

## Known environment limitation

LibreOffice (`soffice --headless --convert-to pdf`) fails to load *any*
source file in this sandbox (`Error: source file could not be loaded`, even
for a trivial .txt) — confirmed not a permissions/sandbox issue (same result
with the sandbox disabled). Actual rendered A4 page counts could not be
verified by direct PDF conversion. Page-count QC instead uses structural
calibration against the approved Lesson 0001 (same font/margins/line
spacing; lesson turn-count and word-count kept in the same range as the
approved exemplar, which is documented as satisfying "5 full A4 pages").
If a future session has a working LibreOffice/render path, prefer real
PDF page counts over this calibration.

## Rules carried forward for every future lesson (from the FINAL MASTER LOCK)

- Ms Lan is the fixed main character in every lesson; exactly ONE named
  Mr/Ms secondary character per lesson; exactly TWO active speakers.
- A0 (0001-0250) / A1 (0251-0600): ~1,000-1,200 English words / 5
  English-only pages per lesson. A2-B2 (0601-2000): 16 English-only pages
  per lesson (much longer — will need a different combination strategy,
  likely one lesson per delivery, per the FINAL MASTER LOCK A2-B2 export
  rule).
- Zero exact duplicate English lines/sentences — check both within a lesson
  and against every other lesson already written (see `build_combined.py`'s
  cross-lesson check; extend its `LESSONS_NEW` list as lessons accumulate).
- Vietnamese must be natural/contextual (never word-for-word), with
  relationship-appropriate pronouns (Ms Lan and same-generation peers use
  chị/anh reciprocally; adjust for family/age relationships as needed).
- Never use name/number/time/object/place substitution to pad length —
  every scene must be a genuinely distinct situation.
