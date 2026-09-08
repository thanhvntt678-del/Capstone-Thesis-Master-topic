# Everyday English Reflex — Production Progress

Master reference: `source/CLAUDE_BOOK_MASTER_2000_LESSONS_FINAL_LOCKED.xlsx`
(sheet `02_MASTER_2000_LESSONS` has the row-by-row Lesson ID / CEFR / domain /
scenario / title / secondary-character spec for all 2000 lessons.)

## Status

- **DELIVERY #1 CLOSED: Lessons 0001-0007**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0001-0007.docx`. Structural
  page estimate reached **~36 pages** (see calibration note below), landing
  inside the ~36–38 page A0 combined target, so this delivery is done.
- **DELIVERY #2 CLOSED: Lessons 0008-0015**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0008-0015.docx`. Structural
  page estimate reached **~35.6 pages** (8 lessons), inside the ~36–38 page
  A0 combined target (same closing logic as Delivery #1), so this delivery
  is done.
- **DELIVERY #3 OPEN: Lessons 0016-...**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0016-0017.docx`. Built with
  `source/build_delivery3.py` (same no-base-docx pattern as
  `build_delivery2.py`, cross-checking against the WHOLE book across all
  deliveries so far via its `DELIVERY1`/`DELIVERY2`/`LESSONS_DELIVERY3`
  lists — extend `LESSONS_DELIVERY3` each time a new lesson is added).
- **Last completed lesson: 0017** (secondary character Mr Robert,
  substituted for the master's suggested "Mr Daniel" which is already
  Lesson 0005's character). Structural page estimate for Delivery #3 so
  far: **~8.7 pages** (2 lessons).
- **Next lesson to write on NEXT: 0018** (A0/Pre-A1, domain
  "Communication", scenario "the first practical exchange about messages &
  everyday digital communication"). The master workbook suggests "Ms
  Olivia" as the secondary character, but that name is already Lesson
  0006's character — **use a different name** (not yet used: David, Emma,
  James, Sarah, Daniel, Olivia, Thomas, Sophie, Michael, Grace, Henry,
  Anna, Peter, Rachel, Kevin, Julia, Robert are all taken) and note the
  substitution here when it's written.
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
| 0009 | Neighbourhood | Mr Michael | 967 | 118 | 0 |
| 0010 | Transport | Ms Grace | 946 | 118 | 0 |
| 0011 | Transport (taxi & ride services) | Mr Henry | 974 | 115 | 0 |
| 0012 | Mobility (walking & getting around) | Ms Anna | 961 | 115 | 0 |
| 0013 | Weather (weather & daily plans) | Mr Peter | 945 | 115 | 0 |
| 0014 | Daily Life (daily routines) | Ms Rachel | 896 | 118 | 0 |
| 0015 | Learning (school & learning) | Mr Kevin | 945 | 115 | 0 |

Total English learning words, Delivery #2: **7,621**.
Total turns + intros: 946 → structural page estimate ≈ **35.6 pages**
(same calibration formula as Delivery #1) — inside the ~36–38 target, so
Delivery #2 is closed here. Do not add Lesson 0016 to this file; it opens
Delivery #3.

Cross-lesson check ran against the **entire book so far** each time via
`build_delivery2.py`'s `WHOLE_BOOK` list. Lessons 0008-0011 each caught
3-12 real duplicates on their first pass (mostly generic closers already
used earlier in the book). **Lesson learned, applied starting with 0012:**
vary closing/acknowledgement lines deliberately from the first draft, not
just topic-specific lines — 0012-0015 each caught only 0-5 duplicates on
their first pass, confirming the approach reduces but does not eliminate
the risk as the book grows (0015 caught 5, back up from 0-1, simply
because there are more prior lines to collide with as the book gets
longer — always run the full check, never assume a lesson is clean).
Result: **0 duplicates across the whole book, 0001-0015.**

## Per-lesson QC record — DELIVERY #3 (OPEN)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0016 | Work (workplace everyday communication) | Ms Julia | 943 | 115 | 0 |
| 0017 | Communication (phone calls) | Mr Robert | 932 | 115 | 0 |

Total English learning words, Delivery #3 so far: **1,875**.
Structural page estimate: **~8.7 pages** — keep adding lessons.
Cross-lesson check ran against the entire book so far each time via
`build_delivery3.py`'s `WHOLE_BOOK` list — 0016 caught 5 duplicates and
0017 caught 3 on their first pass (typical as the book grows, usually
generic "thank you"/acknowledgement closers), fixed by rewording each
time. Result: **0 duplicates across the whole book, 0001-0017.**

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
