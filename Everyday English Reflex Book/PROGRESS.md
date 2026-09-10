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
- **DELIVERY #3 CLOSED: Lessons 0016-0023**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0016-0023.docx`. Structural
  page estimate reached **~35.0 pages** (8 lessons), consistent with
  Delivery #1 (~36.1) and Delivery #2 (~35.6); adding a 9th lesson would
  have risked exceeding the 38-page ceiling, so this delivery closes here.
- **DELIVERY #4 CLOSED: Lessons 0024-0031**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0024-0031.docx`. Structural
  page estimate reached **~34.9 pages** (8 lessons), consistent with
  Deliveries #1-#3 (~35.0-36.1), so this delivery is closed here.
- **DELIVERY #5 CLOSED: Lessons 0032-0039**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0032-0039.docx`. Built with
  `source/build_delivery5.py` (same no-base-docx pattern as
  `build_delivery4.py`, cross-checking against the WHOLE book across all
  deliveries so far via its `DELIVERY1`-`DELIVERY4`/`LESSONS_DELIVERY5`
  lists). Structural page estimate reached **~34.9 pages** (8 lessons,
  matching Delivery #4 almost exactly), so this delivery is closed here
  too.
- **DELIVERY #6 CLOSED: Lessons 0040-0047**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0040-0047.docx`. Structural
  page estimate reached **~34.7 pages** (8 lessons), consistent with all
  prior deliveries, so this delivery is closed here.
- **DELIVERY #7 CLOSED: Lessons 0048-0055**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0048-0055.docx`. Built with
  `source/build_delivery7.py` (same no-base-docx pattern as
  `build_delivery6.py`, cross-checking against the WHOLE book across all
  deliveries so far via its `DELIVERY1`-`DELIVERY6`/`LESSONS_DELIVERY7`
  lists). Structural page estimate reached **~34.3 pages** (8 lessons),
  consistent with all prior deliveries, so this delivery is closed here.
- **DELIVERY #8 OPEN: Lessons 0056-...**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0056-0059.docx`. Built with
  `source/build_delivery8.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#7 plus this one).
  Structural page estimate so far: **~17.4 pages** (4 lessons) — will
  carry over into the next checkpoint block.
- **CHECKPOINT CADENCE (per user instruction 2026-09-09): work proceeds
  in BLOCKS of 10 lessons.** After each block of 10 is written and QC'd, a
  checkpoint report is produced and the user is asked ONCE whether they
  want changes before the next block starts. A block boundary does not
  have to align with a delivery-file boundary — delivery files still
  close whenever the ~36-38 page structural estimate is reached (has been
  averaging 8 lessons per delivery), independent of the 10-lesson
  checkpoint cadence. **BLOCK 0030-0039 completed** (10/10). **BLOCK
  0040-0049 completed** (10/10). **BLOCK 0050-0059 is now COMPLETE**
  (10/10 lessons, written and QC'd in one pass per the user's "NEXT"
  authorization at the prior checkpoint, no per-lesson confirmation).
  Next block: **0060-0069**, to start only after the user responds (any
  reply, including "NEXT", authorizes it; specific feedback is applied
  first).
- **Last completed lesson: 0059** (secondary character Mr Roy, substituted
  for the master's suggested name already in use elsewhere). Domain
  "Family", scenario "a simple family relationship"; confirmed zero
  duplicate lines against the whole book after fixing 2 first-pass
  collisions on the final whole-book check.
- **Next lesson to write on NEXT: 0060** (A0/Pre-A1, domain "Food",
  scenario "saying you are hungry or thirsty", title "Recognising and
  responding to saying you are hungry or thirsty"). The master workbook
  suggests "Ms Anna" as the secondary character, but that name is already
  Lesson 0012's character — **use a different name** (not yet used:
  David, Emma, James, Sarah, Daniel, Olivia, Thomas, Sophie, Michael,
  Grace, Henry, Anna, Peter, Rachel, Kevin, Julia, Robert, Natalie,
  Simon, Diana, George, Laura, Edward, Claire, Nathan, Karen, Patrick,
  Helen, Victor, Susan, Frank, Fiona, Adam, Wendy, Charles, Amy, Jason,
  Linda, Oscar, Paula, Martin, Vivian, Gordon, Ruth, Dennis, Sandra,
  Bruce, Carol, Alan, Joyce, Walter, Cheryl, Roger, Brenda, Steven,
  Janet, Philip, Denise, Roy are all taken — e.g. "Ms Teresa" is a
  reasonable fresh choice) and note the substitution here when it's
  written.
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

## Per-lesson QC record — DELIVERY #3 (CLOSED)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0016 | Work (workplace everyday communication) | Ms Julia | 943 | 115 | 0 |
| 0017 | Communication (phone calls) | Mr Robert | 932 | 115 | 0 |
| 0018 | Communication (messages & digital communication) | Ms Natalie | 954 | 115 | 0 |
| 0019 | Personal Identity (how to spell your name) | Mr Simon | 954 | 109 | 0 |
| 0020 | Social Basics (responding to a greeting) | Ms Diana | 905 | 124 | 0 |
| 0021 | Numbers and Time (a phone number) | Mr George | 1219 | 115 | 0 |
| 0022 | Home (a common household object) | Ms Laura | 1015 | 115 | 0 |
| 0023 | Family (a family member's name) | Mr Edward | 1150 | 115 | 0 |

Total English learning words, Delivery #3: **8,072**.
Total turns + intros: 915 → structural page estimate ≈ **35.0 pages**
(same calibration formula as Deliveries #1-#2) — consistent with the
~36-38 target (a 9th lesson risked exceeding 38 pages), so Delivery #3 is
closed here. Do not add Lesson 0024 to this table; it opens Delivery #4.

Cross-lesson check ran against the entire book so far each time via
`build_delivery3.py`'s `WHOLE_BOOK` list — 0016 caught 5, 0017 caught 3,
0018 caught 5, 0019 caught 1 (against Lesson 0001, expected given the
topic overlap), 0020 caught 0, 0021 caught 4, 0022 caught 1 (a generic
acknowledgement line already used in Lesson 0006), 0023 caught 0
duplicates on their first pass — all fixed by rewording. Lesson 0019
additionally needed 9 within-lesson lines reworded because its "spell the
name" content naturally repeats short answers like "S-I-M-O-N" — each
occurrence had to be wrapped in different surrounding words to stay a
unique full line. Result: **0 duplicates across the whole book,
0001-0023.**

## Per-lesson QC record — DELIVERY #4 (OPEN)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0024 | Food (choosing a drink) | Ms Claire | 1086 | 115 | 0 |
| 0025 | Shopping (a routine everyday need involving shopping & payments) | Mr Nathan | 1040 | 115 | 0 |
| 0026 | Clothing (a routine everyday need involving clothing & personal items) | Ms Karen | 1145 | 115 | 0 |
| 0027 | Neighbourhood (a routine everyday need involving neighbourhood & directions) | Mr Patrick | 1146 | 115 | 0 |
| 0028 | Transport (a routine everyday need involving public transport) | Ms Helen | 1068 | 115 | 0 |
| 0029 | Transport (a routine everyday need involving taxi & ride services) | Mr Victor | 1147 | 115 | 0 |
| 0030 | Mobility (a routine everyday need involving walking & getting around) | Ms Susan | 1120 | 115 | 0 |
| 0031 | Weather (a routine everyday need involving weather & daily plans) | Mr Frank | 1075 | 115 | 0 |

Total English learning words, Delivery #4: **8,827**.
Total turns + intros: 928 → structural page estimate ≈ **34.9 pages**
(same calibration formula as prior deliveries) — consistent with the
~36-38 target (a 9th lesson would have pushed past ~39 pages), so
Delivery #4 is closed here. Do not add Lesson 0032 to this table; it
opens Delivery #5.

Cross-lesson check ran against the entire book so far via
`build_delivery4.py`'s `WHOLE_BOOK` list — 0024 caught 0, 0025 caught 4
(generic short acknowledgement lines already used earlier in the book, one
against Lesson 0007's "No problem, do you have the receipt?" wording),
0026 caught 1 (against Lesson 0006, needed two reword attempts since the
first replacement also collided with the same earlier line), 0027 caught
5 (generic short acknowledgement/relief lines already used earlier in the
book), 0028 caught 1 (against Lesson 0010), 0029 caught 0, 0030 caught 5,
0031 caught 2 (generic acknowledgement lines already used earlier in the
book) duplicates on their first pass — fixed by rewording. Result: **0
duplicates across the whole book, 0001-0031.**

## Per-lesson QC record — DELIVERY #5 (CLOSED)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0032 | Daily Life (a routine everyday need involving daily routines) | Ms Fiona | 1083 | 115 | 0 |
| 0033 | Learning (a routine everyday need involving school & learning) | Mr Adam | 1126 | 115 | 0 |
| 0034 | Work (a routine everyday need involving workplace everyday communication) | Ms Wendy | 1146 | 115 | 0 |
| 0035 | Communication (a routine everyday need involving phone calls) | Mr Charles | 1101 | 115 | 0 |
| 0036 | Communication (a routine everyday need involving messages & everyday digital communication) | Ms Amy | 1100 | 115 | 0 |
| 0037 | Personal Identity (where you are from) | Mr Jason | 1201 | 115 | 0 |
| 0038 | Social Basics (saying goodbye) | Ms Linda | 1156 | 115 | 0 |
| 0039 | Numbers and Time (a price) | Mr Oscar | 1148 | 115 | 0 |

Total English learning words, Delivery #5: **9,061**.
Total turns + intros: 928 → structural page estimate ≈ **34.9 pages**
(same calibration formula, essentially identical to Delivery #4's
profile since every lesson in this stretch used exactly 115 turns) —
consistent with the ~36-38 target, so Delivery #5 is closed here too.

Cross-lesson check ran against the entire book so far via
`build_delivery5.py`'s `WHOLE_BOOK` list (covering Deliveries #1-#4 plus
this one) — 0032 caught 1, 0033 caught 4, 0034 caught 3 (one fix needed a
second reword attempt after the first replacement also collided), 0035
caught 1, 0036 caught 2, 0037 caught 0, 0038 caught 0, 0039 caught 0
duplicates on their first pass (generic short acknowledgement/thank-you
lines already used earlier in the book each time) — all fixed by
rewording. Result: **0 duplicates across the whole book, 0001-0039.**

## Per-lesson QC record — DELIVERY #6 (CLOSED)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0040 | Home (where an object is) | Ms Paula | 1057 | 115 | 0 |
| 0041 | Family (how many people are in the family) | Mr Martin | 1210 | 115 | 0 |
| 0042 | Food (choosing a simple food) | Ms Vivian | 1114 | 115 | 0 |
| 0043 | Shopping (checking an important detail about shopping & payments) | Mr Gordon | 1171 | 115 | 0 |
| 0044 | Clothing (checking an important detail about clothing & personal items) | Ms Ruth | 1225 | 115 | 0 |
| 0045 | Neighbourhood (checking an important detail about neighbourhood & directions) | Mr Dennis | 1223 | 109 | 0 |
| 0046 | Transport (checking an important detail about public transport) | Ms Sandra | 1186 | 115 | 0 |
| 0047 | Transport (checking an important detail about taxi & ride services) | Mr Bruce | 1234 | 115 | 0 |

Total English learning words, Delivery #6: **9,420**.
Total turns + intros: 922 → structural page estimate ≈ **34.7 pages** —
consistent with the ~36-38 target, so Delivery #6 is closed here.

Cross-lesson check ran against the entire book so far via
`build_delivery6.py`'s `WHOLE_BOOK` list (covering Deliveries #1-#5 plus
this one) — this stretch of 8 lessons (all built around a repeated
"confirming/checking a detail" sentence pattern) caught 15 first-pass
collisions in total, mostly generic short confirmations like "Great, I
will take this one then." / "Thanks, I will note that down." reused
across lessons in this very similar scenario type — all fixed by
rewording. Result: **0 duplicates across the whole book, 0001-0047.**
**Lesson learned:** the "checking/confirming a detail" scenario type
(introduced at Lesson 0043) produces noticeably more short-acknowledgement
collisions than topic-varied lessons — worth extra care rewording
closers for any future lesson using this same title pattern.

## Per-lesson QC record — DELIVERY #7 (CLOSED)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0048 | Mobility (checking an important detail about walking & getting around) | Ms Carol | 1242 | 106 | 0 |
| 0049 | Weather (checking an important detail about weather & daily plans) | Mr Alan | 1230 | 109 | 0 |
| 0050 | Daily Life (checking an important detail about daily routines) | Ms Joyce | 1167 | 115 | 0 |
| 0051 | Learning (checking a detail about school & learning) | Mr Walter | 1170 | 115 | 0 |
| 0052 | Work (checking a detail about workplace everyday communication) | Ms Cheryl | 1205 | 115 | 0 |
| 0053 | Communication (checking a detail about phone calls) | Mr Roger | 1213 | 115 | 0 |
| 0054 | Communication (checking a detail about messages & everyday digital communication) | Ms Brenda | 1190 | 115 | 0 |
| 0055 | Personal Identity (where you live) | Mr Steven | 1191 | 115 | 0 |

Total English learning words, Delivery #7: **9,608**.
Structural page estimate ≈ **34.3 pages** — inside the ~36-38 target, so
Delivery #7 is closed here. Do not add Lesson 0056 to this table; it
opens Delivery #8.

Cross-lesson check ran against the entire book so far via
`build_delivery7.py`'s `WHOLE_BOOK` list — 0048 caught 3, 0049 caught 1
duplicates on their first pass (same "checking/confirming a detail"
short-acknowledgement pattern as Delivery #6); 0050-0055 caught 7
first-pass collisions in total (mostly generic closing/acknowledgement
lines already used earlier, including two collisions between 0050 and
0051's own closing lines) — all fixed by rewording. Result: **0
duplicates across the whole book, 0001-0055.**

## Per-lesson QC record — DELIVERY #8 (OPEN)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0056 | Social Basics (saying thank you) | Ms Janet | 1134 | 115 | 0 |
| 0057 | Numbers and Time (today's date) | Mr Philip | 1232 | 115 | 0 |
| 0058 | Home (something you need at home) | Ms Denise | 1138 | 115 | 0 |
| 0059 | Family (a simple family relationship) | Mr Roy | 1163 | 115 | 0 |

Total English learning words, Delivery #8 so far: **4,667**.
Structural page estimate: **~17.4 pages** (4 lessons) — keep adding
lessons.

Cross-lesson check ran against the entire book so far via
`build_delivery8.py`'s `WHOLE_BOOK` list — final whole-book check (0001
through 0059) caught 5 remaining collisions on lessons 0055/0057/0059
(generic short lines already used earlier in the book) — all fixed by
rewording. Result: **0 duplicates across the whole book, 0001-0059.**
**Lesson learned (Lesson 0057, "today's date"):** any lesson whose
scenario is "confirming/repeating a fixed piece of information" (a date,
a spelled name, etc.) needs the answer phrasing deliberately varied
across every repetition from the first draft — 0057 needed 6 separate
within-lesson duplicate patterns reworded (the same date/question
recurring many times by design) before it passed QC.

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

## Checkpoint cadence (added 2026-09-09, supplements — does not replace — the rules below)

- Work proceeds in BLOCKS of 10 lessons (e.g. 0040-0049, 0050-0059, ...).
- Within a block: write and QC every lesson exactly as before; do not ask
  the user "next" after each individual lesson; do not stop mid-block
  without a real technical blocker.
- After each block of 10 is complete: produce a CHECKPOINT report (each
  lesson's domain/scenario/speakers/EN words/turns/duplicate
  counts/page count/file/QC result, plus a block summary with
  COMPLETED/TOTAL PROGRESS/QC PASS-FAIL lines), then ask the user ONCE
  whether they want any changes, then WAIT for a reply before starting
  the next block. Any reply (including a bare "NEXT") authorizes the
  next block; specific feedback is applied first, then the next block
  starts.
- All QC/format/duplicate/character/page-count standards below remain
  100% unchanged — the checkpoint only changes how often user
  confirmation is requested, not what must be checked.

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
