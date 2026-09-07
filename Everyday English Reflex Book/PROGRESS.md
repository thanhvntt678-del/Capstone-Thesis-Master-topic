# Everyday English Reflex — Production Progress

Master reference: `source/CLAUDE_BOOK_MASTER_2000_LESSONS_FINAL_LOCKED.xlsx`
(sheet `02_MASTER_2000_LESSONS` has the row-by-row Lesson ID / CEFR / domain /
scenario / title / secondary-character spec for all 2000 lessons.)

## Status

- **DELIVERY #1 CLOSED: Lessons 0001-0007**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0001-0007.docx`. Structural
  page estimate reached **~36 pages** (see calibration note below), landing
  inside the ~36–38 page A0 combined target, so this delivery is done.
- **DELIVERY #2 OPEN: Lessons 0008-...**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0008-0008.docx` (filename's
  lesson range grows as lessons are added — always rename/replace to match
  the current last lesson, and delete the previous file, same as Delivery
  #1's pattern). Built with `source/build_delivery2.py`, which starts a
  **fresh document with no base docx** (unlike `build_combined.py`, which
  starts from the approved Lesson 0001 file) since 0008+ has no pre-approved
  source — every lesson from 0008 onward is generated the normal way.
  `build_delivery2.py`'s `LESSONS_DELIVERY2` list is what to extend each
  time (append the next lesson's import + list entry), and it already
  cross-checks duplicates against the WHOLE book (Delivery #1's lessons +
  Delivery #2 so far), not just Delivery #2 in isolation.
- **Last completed lesson: 0008.** Structural page estimate for Delivery #2
  so far: **~4.7 pages** (1 lesson) — a long way from the ~36–38 target, so
  expect several more NEXT cycles before Delivery #2 closes.
- **Next lesson to write on NEXT: 0009** (A0/Pre-A1, domain
  "Neighbourhood", scenario "the first practical exchange about
  neighbourhood & directions", secondary character Mr Michael).
- **Interpretation adopted for NEXT** (unchanged going forward): each NEXT
  writes and QCs one more complete lesson, adds it to the current OPEN
  delivery file (`build_delivery2.py` right now), and reports updated
  cumulative counts. Never send a partial lesson; never start a second open
  delivery file while one is still short of the page target. Once Delivery
  #2's estimate lands inside ~36–38 pages, close it (note it CLOSED here,
  same as Delivery #1) and start Delivery #3 the same way Delivery #2
  started — a new `build_deliveryN.py` with no base docx.

## Per-lesson QC record (English learning words, excl. Vietnamese) — DELIVERY #1 (CLOSED)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0001 (approved, preserved) | Personal Identity | Mr David | 829 | 132 | 0 |
| 0002 | Social Basics | Ms Emma | 1018 | 140 | 0 |
| 0003 | Numbers and Time | Mr James | 993 | 141 | 0 |
| 0004 | Home | Ms Sarah | 983 | 139 | 0 |
| 0005 | Family | Mr Daniel | 950 | 143 | 0 |
| 0006 | Food | Ms Olivia | 1007 | 127 | 0 |
| 0007 | Shopping | Mr Thomas | 1006 | 130 | 0 |

Total English learning words, Lessons 0001-0007: **6,786**.
Total turns + intros: 959 → structural page estimate ≈ **36.1 pages**
(see calibration formula below) — inside the ~36–38 target, so Delivery #1
is closed here. Do not add Lesson 0008 to this file; it opens Delivery #2.

Cross-lesson exact-duplicate English line check covers **Lesson 0001 too**
(`build_combined.py`'s `load_lesson0001_as_dict()` parses the approved docx
into the same shape as every other lesson, and `cross_lesson_duplicate_check()`
runs over `[lesson_0001] + LESSONS_NEW`). This caught 7 real duplicates on
the 0006 build and 2 more on the 0007 build (all against lines already used
earlier in the book) — all fixed by rewording. **Always run the full
`build_combined.py` (not a partial manual check) before calling a lesson
done.** Current result for the full 7-lesson book: **0 duplicates.**

## Per-lesson QC record — DELIVERY #2 (OPEN)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0008 | Clothing | Ms Sophie | 987 | 124 | 0 |

Total English learning words, Delivery #2 so far: **987**.
Structural page estimate: **~4.7 pages** — still far below the ~36–38
target; keep adding lessons.

Cross-lesson check for 0008 ran against the **entire book so far**
(0001-0007 + 0008) via `build_delivery2.py`'s `WHOLE_BOOK` list — caught 3
real duplicates on the first pass (against Lessons 0006 and 0007), fixed by
rewording. Result: **0 duplicates across the whole book, 0001-0008.**

**Page-estimate calibration formula** (since real PDF rendering isn't
available — see "Known environment limitation"): approved Lesson 0001 = 132
dialogue turns + 1 intro paragraph = 133 paragraph-units, documented as
satisfying "5 full A4 pages" → **26.6 paragraph-units per page**. For any
lesson set, `estimated_pages = (sum(turns) + count(lessons)) / 26.6`. This
is a rough proxy (assumes uniform paragraph length/wrapping across lessons)
— treat the ~36-38 target as approximate, not exact, and prefer real
rendering the moment it becomes available in this environment.

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
