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
- **DELIVERY #8 CLOSED: Lessons 0056-0063**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0056-0063.docx`. Built with
  `source/build_delivery8.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#7 plus this one).
  Structural page estimate reached **~34.1 pages** (8 lessons), consistent
  with all prior deliveries, so this delivery is closed here.
- **DELIVERY #9 CLOSED: Lessons 0064-0072**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0064-0072.docx`. Built with
  `source/build_delivery9.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#8 plus this one).
  Structural page estimate reached **~36.9 pages** (9 lessons — one more
  than the usual 8 per delivery, since this stretch's turn counts ran
  slightly shorter), still inside the ~36-38 target, so this delivery is
  closed here.
- **DELIVERY #10 CLOSED: Lessons 0073-0081**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0073-0081.docx`. Built with
  `source/build_delivery10.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#9 plus this one).
  Structural page estimate reached **~36.7 pages** (9 lessons), inside
  the ~36-38 target, so this delivery is closed here.
- **DELIVERY #11 CLOSED: Lessons 0082-0090**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0082-0090.docx`. Built with
  `source/build_delivery11.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#10 plus this one).
  Structural page estimate reached **~36.9 pages** (9 lessons), inside
  the ~36-38 target, so this delivery is closed here.
- **DELIVERY #12 CLOSED: Lessons 0091-0099**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0091-0099.docx`. Built with
  `source/build_delivery12.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#11 plus this one).
  Structural page estimate reached **~36.9 pages** (9 lessons), inside
  the ~36-38 target, so this delivery is closed here too — closing
  exactly at the end of Block 0090-0099.
- **DELIVERY #13 CLOSED: Lessons 0100-0108**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0100-0108.docx`. Built with
  `source/build_delivery13.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#12 plus this one).
  Structural page estimate reached **~36.9 pages** (9 lessons), inside
  the ~36-38 target, so this delivery is closed here. Lesson 0109 does
  NOT belong to this delivery; it opens Delivery #14.
- **DELIVERY #14 CLOSED: Lessons 0109-0117**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0109-0117.docx`. Built with
  `source/build_delivery14.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#13 plus this one).
  Structural page estimate reached **~36.9 pages** (9 lessons), inside
  the ~36-38 target, so this delivery is closed here. Lessons 0118-0119
  do NOT belong to this delivery; they open Delivery #15.
- **DELIVERY #15 CLOSED: Lessons 0118-0126**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0118-0126.docx`. Built with
  `source/build_delivery15.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#14 plus this one).
  Structural page estimate reached **~36.9 pages** (9 lessons), inside
  the ~36-38 target, so this delivery is closed here. Lessons 0127-0129
  do NOT belong to this delivery; they open Delivery #16.
- **DELIVERY #16 CLOSED: Lessons 0127-0135**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0127-0135.docx`. Built with
  `source/build_delivery16.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#15 plus this one).
  Structural page estimate reached **~36.9 pages** (9 lessons), inside
  the ~36-38 target, so this delivery is closed here. Lessons 0136-0139
  do NOT belong to this delivery; they open Delivery #17.
- **DELIVERY #17 CLOSED: Lessons 0136-0144**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0136-0144.docx`. Built with
  `source/build_delivery17.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#16 plus this one).
  Structural page estimate reached **~36.9 pages** (9 lessons), inside
  the ~36-38 target, so this delivery is closed here. Lessons 0145-0149
  do NOT belong to this delivery; they open Delivery #18.
- **DELIVERY #18 CLOSED: Lessons 0145-0153**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0145-0153.docx`. Built with
  `source/build_delivery18.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#17 plus this one).
  Structural page estimate reached **~36.9 pages** (9 lessons), inside
  the ~36-38 target, so this delivery is closed here. Lessons 0154-0159
  do NOT belong to this delivery; they open Delivery #19.
- **DELIVERY #19 CLOSED: Lessons 0154-0162**, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0154-0162.docx`. Built with
  `source/build_delivery19.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#18 plus this one).
  Structural page estimate reached **~36.9 pages** (9 lessons), inside
  the ~36-38 target, so this delivery is closed here. Lessons 0163-0169
  do NOT belong to this delivery; they open Delivery #20.
- **DELIVERY #20 OPEN: Lessons 0163-0169** so far, file
  `deliveries/EVERYDAY_ENGLISH_REFLEX_LESSONS_0163-0169.docx`. Built with
  `source/build_delivery20.py` (same no-base-docx pattern, cross-checking
  against the WHOLE book across Deliveries #1-#19 plus this one, 0 dups
  confirmed for 0001-0169). Structural page estimate so far: **~28.7
  pages** (7 lessons) — under the ~36-38 target, so this delivery stays
  open and Block 0170-0179's lessons will be added to it next.
- **CHECKPOINT CADENCE (per user instruction 2026-09-09): work proceeds
  in BLOCKS of 10 lessons.** After each block of 10 is written and QC'd, a
  checkpoint report is produced and the user is asked ONCE whether they
  want changes before the next block starts. A block boundary does not
  have to align with a delivery-file boundary — delivery files still
  close whenever the ~36-38 page structural estimate is reached (has been
  averaging 8-9 lessons per delivery), independent of the 10-lesson
  checkpoint cadence. **BLOCK 0030-0039 completed** (10/10). **BLOCK
  0040-0049 completed** (10/10). **BLOCK 0050-0059 completed** (10/10).
  **BLOCK 0060-0069 completed** (10/10). **BLOCK 0070-0079 completed**
  (10/10). **BLOCK 0080-0089 completed** (10/10). **BLOCK 0090-0099
  completed** (10/10). **BLOCK 0100-0109 completed** (10/10). **BLOCK
  0110-0119 completed** (10/10). **BLOCK 0120-0129 completed** (10/10).
  **BLOCK 0130-0139 completed** (10/10). **BLOCK 0140-0149 completed**
  (10/10). **BLOCK 0150-0159 completed** (10/10). **BLOCK 0160-0169 is
  now COMPLETE** (10/10 lessons, written and QC'd in one pass per the
  user's "next" authorization at the prior checkpoint, no per-lesson
  confirmation). This block continued the "checking an important
  detail about X" pattern for Lessons 0160-0162 (workplace
  communication, phone calls, messages & digital communication), then
  moved into a fresh wave of early-topic revisits for Lessons
  0163-0169: where you live, saying thank you, today's date, something
  you need at home, a simple family relationship, saying you are
  hungry or thirsty, and asking for help with shopping & payments.
  Next block: **0170-0179**, to start only after the user responds
  (any reply, including "NEXT" or "next", authorizes it; specific
  feedback is applied first).
- **Last completed lesson: 0169** (secondary character Mr David).
  Domain "Shopping", scenario "asking for help with shopping &
  payments". Confirmed zero duplicate lines against the whole book,
  0001-0169.
- **Next lesson to write on NEXT: 0170** (A0/Pre-A1 — check the master
  workbook row 171 for exact domain/scenario/title before writing). The
  full cumulative names-used list for secondary characters (do not reuse
  any of these): David, Emma, James, Sarah, Daniel, Olivia, Thomas,
  Sophie, Michael, Grace, Henry, Anna, Peter, Rachel, Kevin, Julia,
  Robert, Natalie, Simon, Diana, George, Laura, Edward, Claire, Nathan,
  Karen, Patrick, Helen, Victor, Susan, Frank, Fiona, Adam, Wendy,
  Charles, Amy, Jason, Linda, Oscar, Paula, Martin, Vivian, Gordon, Ruth,
  Dennis, Sandra, Bruce, Carol, Alan, Joyce, Walter, Cheryl, Roger,
  Brenda, Steven, Janet, Philip, Denise, Roy, Teresa, Colin, Melissa,
  Derek, Sharon, Trevor, Yvonne, Barry, Pamela, Neil, Donna, Harold,
  Gloria, Bernard, Irene, Stanley, Doris, Leonard, Yvette, Clifford,
  Deborah, Russell, Wanda, Gerald, Beverly, Curtis, Sheila, Duane,
  Marilyn, Lawrence, Cassandra, Nelson, Priscilla, Terrence, Loretta,
  Malcolm, Wilma, Herbert, Rosalind, Vernon, Antoinette, Desmond,
  Winifred, Cedric, Geraldine, Ambrose, Henrietta, Percival, Millicent,
  Reginald, Beatrice, Cornelius, Prudence, Aloysius, Fenella, Barnaby,
  Octavia, Humphrey, Rosamund, Bartholomew, Theodora, Bertram, Felicity,
  Montgomery, Araminta, Cuthbert, Philippa, Ignatius, Seraphina, Leopold,
  Wilhelmina, Cordelia, Ezekiel, Perpetua, Anselm, Hyacinth, Evangeline,
  Torvald, Clementine, Osbert, Eulalia, Thaddeus, Cressida, Alaric,
  Dorothea, Silas, Amabel, Gideon, Verity, Oswin, Isolde, Peregrine,
  Marguerite, Quentin, Rosalie, Baldwin, Genevieve, Alistair, Marcella,
  Sylvester, Philomena, Corwin, Delphine, Tobias, Arabella, Jasper,
  Cecily, Lucian, Miranda, Bertrand. Pick a fresh name for Lesson
  0170's secondary character and note the substitution here when it's
  written.
  **Lesson learned from Block 0160-0169 (important process fix):**
  four lessons in this block (0166, 0167, 0168, 0169) initially used
  the master workbook's suggested secondary-character names directly
  (Grace, Henry, Anna, David) instead of substituting a fresh name —
  these were all names already used many lessons earlier (Grace in
  0010, Henry in 0011, Anna in 0012, David in the approved Lesson
  0001), so they were caught only by manually diffing against the
  cumulative names-used list, NOT by the automated `qc_report()` /
  cross-lesson duplicate-line check, which only compares dialogue
  text and has no visibility into character names. Fixed via
  find-and-replace to Cecily, Lucian, Miranda, and Bertrand
  respectively. Going forward, always actively substitute a FRESH name
  for the master workbook's suggested secondary character before
  drafting a lesson, and double-check every new lesson's two speaker
  names against the cumulative names-used list before considering the
  lesson done — the master workbook's suggested names are always
  already used by this point in the book and must never be used as-is.
  **Lesson learned for future "misunderstanding or problem" lessons:**
  this scenario pattern (spanned 0097-0108) is prone to
  short-acknowledgement collision risk — vary "thank you" / "found it" /
  "good idea" / "that makes much more sense now" style closing lines
  deliberately from the first draft.
  **Lesson learned for future single-premise lessons (like "your name",
  "your phone number", etc.):** when every scene's payoff line is
  structurally identical (e.g. "give your name" or "give a phone
  number"), plan distinct openers, sentence structures, AND underlying
  content (different fictional numbers/spellings) for all ~36 payoff
  lines from the first draft rather than reusing the same 1-2 literal
  values with only the surrounding phrasing varied.
  **Lesson learned for the new "asking and answering very simple
  questions about X" pattern (started 0109, continued through 0139):**
  when a lesson revisits an EARLY topic already covered by Lessons
  0002-0031, short generic reply lines ("thank you, I see it now.",
  "that is very convenient, thank you.", "good to know, thank you for
  clarifying.", "thank you, I will head there now.", "that is very kind
  of you.", "one less thing to worry about.") collide heavily with those
  much earlier lessons AND with each other across same-pattern lessons
  in the same block (e.g. two "give a name/number" lessons sharing
  generic "Thank you, X" confirmations) — write reply lines that echo
  back a specific detail from the answer (e.g. "Room B, thank you, I
  will find it." instead of "Thank you, I will head there now.") to keep
  them naturally unique from the first draft. This pattern is now
  confirmed to run at least through Lesson 0149 and likely continues
  into future blocks — keep applying this rule proactively, especially
  when two lessons in the same block share a very similar "collect a
  detail" structure (e.g. spelling a name and giving a phone number).
  **Lesson learned from Block 0140-0149:** for single-premise
  "revisit" lessons built around a fixed-format answer (a place name, a
  price, a family headcount), reusing the exact same underlying value
  or composition across multiple scenes causes INTERNAL duplication
  even when the surrounding sentence differs only by pronoun or
  reaction — e.g. Lesson 0149 ("how many people are in the family")
  first drafted several third-party families with identical headcounts
  and compositions ("five, parents and three kids" used three times),
  caught and fixed only at the internal `qc_report()` stage. Plan the
  full list of 36 distinct underlying values (names, prices, locations,
  headcounts) BEFORE drafting the dialogue lines for any such lesson,
  not just the surrounding phrasing.
  **Lesson learned for the new "checking an important detail about X"
  pattern (started 0151, continued through 0159):** this scenario
  revisits every domain with a "Can you check if X?" / "Yes/No,
  [detail]." / "Good, [reaction echoing the detail]." structure across
  35 scenes — same generic-reply collision risk as the "asking and
  answering" pattern applies here too. Lessons 0151-0153 (Delivery
  #18) and 0154, 0156, 0158 (Delivery #19) needed rounds of fixes for
  short reactions ("good, that gives us plenty of time.", "good, that
  is a relief to hear.", "good, better safe than sorry.") colliding
  with much earlier lessons — apply the "echo a specific detail from
  the answer" rule proactively from the first draft here too, not just
  for the "asking and answering" wave.
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

## Per-lesson QC record — DELIVERY #8 (CLOSED)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0056 | Social Basics (saying thank you) | Ms Janet | 1134 | 115 | 0 |
| 0057 | Numbers and Time (today's date) | Mr Philip | 1232 | 115 | 0 |
| 0058 | Home (something you need at home) | Ms Denise | 1138 | 115 | 0 |
| 0059 | Family (a simple family relationship) | Mr Roy | 1163 | 115 | 0 |
| 0060 | Food (saying you are hungry or thirsty) | Ms Teresa | 1299 | 114 | 0 |
| 0061 | Shopping (asking for help with shopping & payments) | Mr Colin | 1203 | 108 | 0 |
| 0062 | Clothing (asking for help with clothing & personal items) | Ms Melissa | 1217 | 108 | 0 |
| 0063 | Neighbourhood (asking for help with neighbourhood & directions) | Mr Derek | 1249 | 108 | 0 |

Total English learning words, Delivery #8: **9,635**.
Structural page estimate ≈ **34.1 pages** — inside the ~36-38 target, so
Delivery #8 is closed here. Do not add Lesson 0064 to this table; it
opens Delivery #9.

Cross-lesson check ran against the entire book so far via
`build_delivery8.py`'s `WHOLE_BOOK` list — final whole-book check (0001
through 0063) caught 10 collisions on lessons 0060/0061/0062/0063
(generic short lines like "Thank you, I will head there now." already
used earlier in the book) — all fixed by rewording. Result: **0
duplicates across the whole book, 0001-0063.**
**Lesson learned (Lesson 0057, "today's date"):** any lesson whose
scenario is "confirming/repeating a fixed piece of information" (a date,
a spelled name, etc.) needs the answer phrasing deliberately varied
across every repetition from the first draft — 0057 needed 6 separate
within-lesson duplicate patterns reworded (the same date/question
recurring many times by design) before it passed QC.

## Per-lesson QC record — DELIVERY #9 (CLOSED)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0064 | Transport (asking for help with public transport) | Ms Sharon | 1279 | 108 | 0 |
| 0065 | Transport (asking for help with taxi & ride services) | Mr Trevor | 1268 | 108 | 0 |
| 0066 | Mobility (asking for help with walking & getting around) | Ms Yvonne | 1287 | 108 | 0 |
| 0067 | Weather (asking for help with weather & daily plans) | Mr Barry | 1343 | 108 | 0 |
| 0068 | Daily Life (asking for help with daily routines) | Ms Pamela | 1240 | 108 | 0 |
| 0069 | Learning (asking for help with school & learning) | Mr Neil | 1217 | 108 | 0 |
| 0070 | Work (asking for help with workplace everyday communication) | Ms Donna | 1237 | 108 | 0 |
| 0071 | Communication (asking for help with phone calls) | Mr Harold | 1276 | 108 | 0 |
| 0072 | Communication (asking for help with messages & everyday digital communication) | Ms Gloria | 1226 | 108 | 0 |

Total English learning words, Delivery #9: **11,373**.
Structural page estimate ≈ **36.9 pages** — inside the ~36-38 target, so
Delivery #9 is closed here. Do not add Lesson 0073 to this table; it
opens Delivery #10.

Cross-lesson check ran against the entire book so far via
`build_delivery9.py`'s `WHOLE_BOOK` list — the "asking for help with X"
scenario pattern that runs from Lesson 0061 through 0072 produced a large
batch of first-pass collisions each time (25 on the 0064-0069 pass, 10
more on the 0070-0072 pass), almost all generic short acknowledgement
lines ("Thank you, that will help a lot.", "Ah, that makes sense now,
thank you.", "Thank you, I will head there now.", etc.) reused across
many "asking for help" lessons in a row — all fixed by rewording,
including self-introduced collisions caught on follow-up full-book
re-runs. Result: **0 duplicates across the whole book, 0001-0072.**
**Lesson learned:** like the "checking/confirming a detail" pattern noted
at Delivery #6, the "asking for help with X" scenario type is prone to
noticeably more short-acknowledgement collisions than topic-varied
lessons — worth extra deliberate variation of "thank you" / "that makes
sense" style closing lines for any future lesson using this same title
pattern. This pattern ended at Lesson 0072 per the master workbook; 0073
onward returns to topic-varied scenario titles.

## Per-lesson QC record — DELIVERY #10 (CLOSED)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0073 | Personal Identity (your age) | Mr Bernard | 1166 | 105 | 0 |
| 0074 | Social Basics (saying sorry) | Ms Irene | 1174 | 105 | 0 |
| 0075 | Numbers and Time (the day of the week) | Mr Stanley | 1130 | 108 | 0 |
| 0076 | Home (opening or closing something) | Ms Doris | 1208 | 108 | 0 |
| 0077 | Family (where a family member is) | Mr Leonard | 1161 | 108 | 0 |
| 0078 | Food (asking what something is) | Ms Yvette | 1142 | 108 | 0 |
| 0079 | Shopping (a change or choice involving shopping & payments) | Mr Clifford | 1192 | 108 | 0 |
| 0080 | Clothing (a change or choice involving clothing & personal items) | Ms Deborah | 1164 | 108 | 0 |
| 0081 | Neighbourhood (a change or choice involving neighbourhood & directions) | Mr Russell | 1235 | 108 | 0 |

Total English learning words, Delivery #10: **10,572**.
Structural page estimate ≈ **36.7 pages** — inside the ~36-38 target, so
Delivery #10 is closed here. Do not add Lesson 0082 to this table; it
opens Delivery #11.

Cross-lesson check ran against the entire book so far via
`build_delivery10.py`'s `WHOLE_BOOK` list — returning to topic-varied
scenarios (age, sorry, day of the week, opening/closing, family member
location, asking what something is) produced far fewer collisions than
the "asking for help" stretch: 6 on the 0073-0079 pass plus 1
self-introduced collision, then the "change or choice" pattern starting
at 0079 picked back up with 8 more collisions on 0080-0081 — all fixed
by rewording. Result: **0 duplicates across the whole book, 0001-0081.**

## Per-lesson QC record — DELIVERY #11 (CLOSED)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0082 | Transport (a change or choice involving public transport) | Ms Wanda | 1190 | 108 | 0 |
| 0083 | Transport (a change or choice involving taxi & ride services) | Mr Gerald | 1242 | 108 | 0 |
| 0084 | Mobility (a change or choice involving walking & getting around) | Ms Beverly | 1234 | 108 | 0 |
| 0085 | Weather (a change or choice involving weather & daily plans) | Mr Curtis | 1253 | 108 | 0 |
| 0086 | Daily Life (a change or choice involving daily routines) | Ms Sheila | 1224 | 108 | 0 |
| 0087 | Learning (a change or choice involving school & learning) | Mr Duane | 1239 | 108 | 0 |
| 0088 | Work (a change or choice involving workplace everyday communication) | Ms Marilyn | 1251 | 108 | 0 |
| 0089 | Communication (a change or choice involving phone calls) | Mr Lawrence | 1265 | 108 | 0 |
| 0090 | Communication (a change or choice involving messages & everyday digital communication) | Ms Cassandra | 1258 | 108 | 0 |

Total English learning words, Delivery #11: **11,156**.
Structural page estimate ≈ **36.9 pages** — inside the ~36-38 target, so
Delivery #11 is closed here. Do not add Lesson 0091 to this table; it
opens Delivery #12.

Cross-lesson check ran against the entire book so far via
`build_delivery11.py`'s `WHOLE_BOOK` list — the "a change or choice
involving X" scenario pattern that runs through this whole block (and
started at Lesson 0079) produced the heaviest collision count of any
block so far: 22 on the 0082-0089 pass plus 1 more on 0090, almost all
generic short lines like "That is exactly why I made the change.",
"Good point, let us stick with that then.", and "Exactly, better safe
than sorry." reused repeatedly across "change or choice" lessons — all
fixed by rewording. Result: **0 duplicates across the whole book,
0001-0090.**
**Lesson learned:** the "change or choice" scenario type is now
confirmed as the most collision-prone pattern encountered yet (worse
than "checking/confirming a detail" and "asking for help with X") —
future lessons using this title pattern should avoid generic
"that is exactly why..." / "good point, let us..." / "exactly, better
safe than sorry" closers from the first draft entirely. This pattern
ended at Lesson 0090 per the master workbook.

## Per-lesson QC record — DELIVERY #12 (CLOSED)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0091 | Personal Identity (your phone number) | Mr Nelson | 1232 | 108 | 0 |
| 0092 | Social Basics (getting someone's attention politely) | Ms Priscilla | 1145 | 108 | 0 |
| 0093 | Numbers and Time (the current time) | Mr Terrence | 1222 | 108 | 0 |
| 0094 | Home (a simple household instruction) | Ms Loretta | 1154 | 108 | 0 |
| 0095 | Family (a simple family plan) | Mr Malcolm | 1210 | 108 | 0 |
| 0096 | Food (a basic meal choice) | Ms Wilma | 1170 | 108 | 0 |
| 0097 | Shopping (a misunderstanding or problem involving shopping & payments) | Mr Herbert | 1257 | 108 | 0 |
| 0098 | Clothing (a misunderstanding or problem involving clothing & personal items) | Ms Rosalind | 1253 | 108 | 0 |
| 0099 | Neighbourhood (a misunderstanding or problem involving neighbourhood & directions) | Mr Vernon | 1275 | 108 | 0 |

Total English learning words, Delivery #12: **10,918**.
Structural page estimate ≈ **36.9 pages** — inside the ~36-38 target, so
Delivery #12 is closed here, exactly at the end of Block 0090-0099. Do
not add Lesson 0100 to this table; it opens Delivery #13.

Cross-lesson check ran against the entire book so far via
`build_delivery12.py`'s `WHOLE_BOOK` list — 27 first-pass collisions on
the final whole-book check, again mostly generic short acknowledgement
lines ("thank you, I really appreciate it.", "found it, thank you for
the tip.", "that makes complete sense, thank you for explaining.", etc.)
reused across Lessons 0091-0099 — all fixed by rewording. Result: **0
duplicates across the whole book, 0001-0099.**
**Lesson learned:** the new "a misunderstanding or problem involving X"
scenario pattern (started at Lesson 0097) shows the same collision risk
as "change or choice" and "asking for help with X" — vary "thank you" /
"found it" / "that makes complete sense" style closing lines
deliberately from the first draft for any future lesson using this
title pattern.

## Per-lesson QC record — DELIVERY #13 (CLOSED)

| Lesson | Domain | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|
| 0100 | Transport (a misunderstanding or problem involving public transport) | Ms Antoinette | 1258 | 108 | 0 |
| 0101 | Transport (a misunderstanding or problem involving taxi & ride services) | Mr Desmond | 1348 | 108 | 0 |
| 0102 | Mobility (a misunderstanding or problem involving walking & getting around) | Ms Winifred | 1296 | 108 | 0 |
| 0103 | Weather (a misunderstanding or problem involving weather & daily plans) | Mr Cedric | 1360 | 108 | 0 |
| 0104 | Daily Life (a misunderstanding or problem involving daily routines) | Ms Geraldine | 1331 | 108 | 0 |
| 0105 | Learning (a misunderstanding or problem involving school & learning) | Mr Ambrose | 1313 | 108 | 0 |
| 0106 | Work (a misunderstanding or problem involving workplace everyday communication) | Ms Henrietta | 1305 | 108 | 0 |
| 0107 | Communication (a misunderstanding or problem involving phone calls) | Mr Percival | 1337 | 108 | 0 |
| 0108 | Communication (a misunderstanding or problem involving messages & everyday digital communication) | Ms Millicent | 1311 | 108 | 0 |

Total English learning words, Delivery #13: **11,859**.
Structural page estimate ≈ **36.9 pages** — inside the ~36-38 target, so
Delivery #13 is closed here. Do not add Lesson 0109 to this table; it
opens Delivery #14 (Lesson 0109 is a "your name" Personal Identity
lesson, not a "misunderstanding or problem" lesson, and is documented
individually in the Status section above).

Cross-lesson check ran against the entire book so far via
`build_delivery13.py`'s `WHOLE_BOOK` list — 22 first-pass collisions on
the final whole-book check for Lessons 0100-0108 (generic short lines
like "Good idea, that should clear it up.", "Thank you, I really
appreciate that.", "Ah, that makes much more sense now.", "Thank you,
that helps a lot.") reused across this block — all fixed by rewording;
two of the reworded replacement lines then collided with each other and
with earlier lessons on a second pass and were reworded again. Result:
**0 duplicates across the whole book, 0001-0108.**
**Lesson learned:** confirms the "misunderstanding or problem involving
X" pattern (now spanning Lessons 0097-0108, 12 lessons) as a
consistently collision-prone pattern — continue varying "thank you" /
"good idea" / "that makes much more sense now" style closers from the
first draft for any remaining lessons of this type.

## Per-lesson QC record — DELIVERY #14 (CLOSED)

| Lesson | Domain | Scenario | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|---|
| 0109 | Personal Identity | your name | Mr Reginald | 1015 | 108 | 0 |
| 0110 | Social Basics | saying hello | Ms Beatrice | 1264 | 108 | 0 |
| 0111 | Numbers and Time | numbers 0-20 | Mr Cornelius | 1039 | 108 | 0 |
| 0112 | Home | a room in the home | Ms Prudence | 1178 | 108 | 0 |
| 0113 | Family | who a family member is | Mr Aloysius | 1181 | 108 | 0 |
| 0114 | Food | asking for water | Ms Fenella | 1412 | 108 | 0 |
| 0115 | Shopping | first practical exchange about shopping & payments | Mr Barnaby | 1118 | 108 | 0 |
| 0116 | Clothing | first practical exchange about clothing & personal items | Ms Octavia | 1136 | 108 | 0 |
| 0117 | Neighbourhood | first practical exchange about neighbourhood & directions | Mr Humphrey | 1146 | 108 | 0 |

Total English learning words, Delivery #14: **10,489**.
Structural page estimate ≈ **36.9 pages** — inside the ~36-38 target, so
Delivery #14 is closed here. Do not add Lessons 0118-0119 to this
table; they open Delivery #15 (documented individually in the Status
section above).

Cross-lesson check ran against the entire book so far via
`build_delivery14.py`'s `WHOLE_BOOK` list — 20 first-pass collisions on
the final whole-book check for Lessons 0109-0117, concentrated in
Lessons 0115-0117 (the "first practical exchange about X" scenes for
shopping, clothing, and neighbourhood/directions), because these
revisit topics already covered by Lessons 0004, 0006, 0007, 0009,
0010, 0011, 0025, 0061, 0063, 0065, 0078, and 0091, producing generic
reply-line collisions ("thank you, I see it now.", "that is very
convenient, thank you.", "good to know, thank you for clarifying.") —
all fixed by rewording (one fix in Lesson 0115 briefly created a new
within-lesson duplicate against an existing line, caught and reworded
again). Result: **0 duplicates across the whole book, 0001-0117.**
**Lesson learned:** the new "asking and answering very simple questions
about X" pattern (started at Lesson 0109) is especially collision-prone
whenever the topic overlaps an EARLY lesson (0002-0031) — for any
future lesson of this type covering an already-used topic, write reply
lines that echo a specific detail from the answer just given, rather
than a generic "thank you, that is very helpful" style closer.

## Per-lesson QC record — DELIVERY #15 (CLOSED)

| Lesson | Domain | Scenario | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|---|
| 0118 | Transport | first practical exchange about public transport | Ms Rosamund | 1135 | 108 | 0 |
| 0119 | Transport | first practical exchange about taxi & ride services | Mr Bartholomew | 1182 | 108 | 0 |
| 0120 | Mobility | first practical exchange about walking & getting around | Ms Theodora | 1222 | 108 | 0 |
| 0121 | Weather | first practical exchange about weather & daily plans | Mr Bertram | 1193 | 108 | 0 |
| 0122 | Daily Life | first practical exchange about daily routines | Ms Felicity | 1186 | 108 | 0 |
| 0123 | Learning | first practical exchange about school & learning | Mr Montgomery | 1176 | 108 | 0 |
| 0124 | Work | first practical exchange about workplace everyday communication | Ms Araminta | 1182 | 108 | 0 |
| 0125 | Communication | first practical exchange about phone calls | Mr Cuthbert | 1379 | 108 | 0 |
| 0126 | Communication | first practical exchange about messages & everyday digital communication | Ms Philippa | 1240 | 108 | 0 |

Total English learning words, Delivery #15: **10,896**.
Structural page estimate ≈ **36.9 pages** — inside the ~36-38 target, so
Delivery #15 is closed here. Do not add Lessons 0127-0129 to this
table; they open Delivery #16 (documented individually in the Status
section above).

Cross-lesson check ran against the entire book so far via
`build_delivery15.py`'s `WHOLE_BOOK` list — 38 first-pass collisions on
the final whole-book check for Lessons 0118-0126, spread across nearly
every lesson in the block, all generic reply lines ("thank you, I will
head there now.", "perfect, that is very convenient.", "good to know,
thank you.", "thank you, I found it now.") colliding with much earlier
lessons (0004-0117 range) — all fixed by rewording to echo a specific
detail from the answer instead of a generic closer; one fix
accidentally targeted the wrong scene's context on the first pass and
was corrected. A second whole-book pass after fixes found one more
collision ("there is a machine right by the entrance." vs Lesson 0010),
also fixed by rewording. Result: **0 duplicates across the whole book,
0001-0126.**
**Lesson learned:** confirms the "asking and answering very simple
questions about X" pattern remains highly collision-prone against
Lessons 0002-0031 for every lesson that revisits an early topic — the
"echo a specific detail from the answer" rule (documented after
Delivery #14) needs to be applied proactively from the very first draft
of each such lesson, not just after the whole-book check flags
collisions, to avoid repeated rounds of fixes.

## Per-lesson QC record — DELIVERY #16 (CLOSED)

| Lesson | Domain | Scenario | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|---|
| 0127 | Personal Identity | how to spell your name | Mr Ignatius | 1152 | 108 | 0 |
| 0128 | Social Basics | responding to a greeting | Ms Seraphina | 1381 | 108 | 0 |
| 0129 | Numbers and Time | a phone number | Mr Leopold | 1233 | 108 | 0 |
| 0130 | Home | a common household object | Ms Cordelia | 1080 | 108 | 0 |
| 0131 | Family | a family member's name | Mr Wilfred | 1005 | 108 | 0 |
| 0132 | Food | choosing a drink | Ms Perpetua | 1190 | 108 | 0 |
| 0133 | Shopping | routine everyday need — shopping & payments | Mr Ezekiel | 1168 | 108 | 0 |
| 0134 | Clothing | routine everyday need — clothing & personal items | Ms Evangeline | 1164 | 108 | 0 |
| 0135 | Neighbourhood | routine everyday need — neighbourhood & directions | Mr Anselm | 1284 | 108 | 0 |

Total English learning words, Delivery #16: **10,657**.
Structural page estimate ≈ **36.9 pages** — inside the ~36-38 target, so
Delivery #16 is closed here. Do not add Lessons 0136-0139 to this
table; they open Delivery #17 (documented individually in the Status
section above).

Cross-lesson check ran against the entire book so far via
`build_delivery16.py`'s `WHOLE_BOOK` list — 27 first-pass collisions on
the final whole-book check for Lessons 0127-0135, mostly generic
"thank you, X" / spelling-confirmation reply lines colliding with much
earlier lessons, plus (newly observed) several of Lesson 0129's
"collect one piece of information" reply lines colliding with Lesson
0127's similarly generic reply lines from the SAME block — all fixed
by rewording the later-appearing line to echo a specific detail from
its own answer. A second whole-book pass after fixes found 0 remaining
collisions. Result: **0 duplicates across the whole book, 0001-0135.**
Lessons 0127 and 0129 also required full internal rewrites before the
cross-lesson check: 0127 was short at 105 turns with 3 spelling-answer
lines each repeated up to 5 times, fixed by adding a 36th scene and
rewriting all spelling-answer lines with unique phrasing; 0129 was the
most severe internal-duplication case seen so far — only 2 literal
phone numbers reused across all 36 scenes with ~6-7 templates repeated
up to 6 times each — fixed via a complete rewrite generating 36
distinct fictional phone numbers, each spelled out digit-by-digit.
**Lesson learned:** the "asking and answering very simple questions
about X" pattern's collision risk is not limited to old lessons —
within a single block, two lessons that share a similar "collect one
piece of information" structure (e.g. spelling a name, giving a phone
number) can also collide with EACH OTHER on their generic confirmation
closers. When drafting such lessons, check the other lessons already
planned for the same block for structural similarity and pre-vary the
closer phrasing accordingly, in addition to the existing "echo a
specific detail" rule.

## Per-lesson QC record — DELIVERY #17 (CLOSED)

| Lesson | Domain | Scenario | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|---|
| 0136 | Transport | routine everyday need — public transport | Ms Hyacinth | 1262 | 108 | 0 |
| 0137 | Transport | routine everyday need — taxi & ride services | Mr Torvald | 1274 | 108 | 0 |
| 0138 | Mobility | routine everyday need — walking & getting around | Ms Clementine | 1271 | 108 | 0 |
| 0139 | Weather | routine everyday need — weather & daily plans | Mr Osbert | 1331 | 108 | 0 |
| 0140 | Daily Life | routine everyday need — daily routines | Ms Eulalia | 1251 | 108 | 0 |
| 0141 | Learning | routine everyday need — school & learning | Mr Thaddeus | 1256 | 108 | 0 |
| 0142 | Work | routine everyday need — workplace communication | Ms Cressida | 1256 | 108 | 0 |
| 0143 | Communication | routine everyday need — phone calls | Mr Alaric | 1333 | 108 | 0 |
| 0144 | Communication | routine everyday need — messages & digital communication | Ms Dorothea | 1242 | 108 | 0 |

Total English learning words, Delivery #17: **11,476**.
Structural page estimate ≈ **36.9 pages** — inside the ~36-38 target, so
Delivery #17 is closed here. Do not add Lessons 0145-0149 to this
table; they open Delivery #18 (documented individually below).

Cross-lesson check ran against the entire book so far via
`build_delivery17.py`'s `WHOLE_BOOK` list — 15 first-pass collisions
on the final whole-book check, spread across Lessons 0136-0139 (which
had never been through a whole-book cross-check before, since Delivery
#16 closed at 0135) and Lessons 0143/0144, mostly generic reply lines
("good, that is a relief to hear.", "great, one less thing to worry
about.", "good, i will read it before we start.") colliding with much
earlier lessons. All fixed by rewording the later-appearing line to
echo a specific detail from its own answer. A second whole-book pass
after fixes found 0 remaining collisions. Result: **0 duplicates
across the whole book, 0001-0144.**

## Per-lesson QC record — DELIVERY #18 (CLOSED)

| Lesson | Domain | Scenario | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|---|
| 0145 | Personal Identity | where you are from | Mr Silas | 1275 | 108 | 0 |
| 0146 | Social Basics | saying goodbye | Ms Amabel | 1293 | 108 | 0 |
| 0147 | Numbers and Time | a price | Mr Gideon | 1338 | 108 | 0 |
| 0148 | Home | where an object is | Ms Verity | 1142 | 108 | 0 |
| 0149 | Family | how many people are in the family | Mr Oswin | 1457 | 108 | 0 |
| 0150 | Food | choosing a simple food | Ms Isolde | 1018 | 108 | 0 |
| 0151 | Shopping | checking an important detail — shopping & payments | Mr Peregrine | 1177 | 108 | 0 |
| 0152 | Clothing | checking an important detail — clothing & personal items | Ms Marguerite | 1221 | 108 | 0 |
| 0153 | Neighbourhood | checking an important detail — neighbourhood & directions | Mr Quentin | 1290 | 108 | 0 |

Total English learning words, Delivery #18: **11,211**.
Structural page estimate ≈ **36.9 pages** — inside the ~36-38 target,
so Delivery #18 is closed here. Do not add Lessons 0154-0159 to this
table; they open Delivery #19 (documented individually below).

Cross-lesson check ran against the entire book so far via
`build_delivery18.py`'s `WHOLE_BOOK` list — Lessons 0145-0149 were
clean against the whole book on the first pass (0 collisions), but
adding Lessons 0150-0153 to the same delivery surfaced 9 first-pass
collisions on the final whole-book check, all short generic reactions
("good, that gives us plenty of time.", "good, that matches what I
expected.", "good, that is reassuring to hear.") colliding with much
earlier lessons. All fixed by rewording the later-appearing line to
echo a specific detail from its own answer. A second whole-book pass
after fixes found 0 remaining collisions. Result: **0 duplicates
across the whole book, 0001-0153.**
**Lesson learned:** Lessons 0145, 0147, and 0149 are single-premise
"revisit" lessons (where you are from / a price / family headcount)
built around 36 distinct third-party subjects or values planned BEFORE
drafting dialogue — this upfront planning is what kept them clean on
the first whole-book pass, in contrast to earlier single-premise
lessons (0109, 0127, 0129) that needed full rewrites after the fact.
Lesson 0149 still needed one round of INTERNAL fixes for repeated
family compositions (see the Block 0140-0149 note in the Status
section above) — planning distinct openers is not enough on its own;
the underlying values themselves must all be distinct too. Lesson 0150
opened the new "checking an important detail about X" pattern
(Lessons 0151-0153); this pattern's short "Good, [reaction]" closers
are just as collision-prone as the earlier "asking and answering"
pattern's closers.

## Per-lesson QC record — DELIVERY #19 (CLOSED)

| Lesson | Domain | Scenario | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|---|
| 0154 | Transport | checking an important detail — public transport | Ms Rosalie | 1267 | 108 | 0 |
| 0155 | Transport | checking an important detail — taxi & ride services | Mr Baldwin | 1286 | 108 | 0 |
| 0156 | Mobility | checking an important detail — walking & getting around | Ms Genevieve | 1267 | 108 | 0 |
| 0157 | Weather | checking an important detail — weather & daily plans | Mr Alistair | 1284 | 108 | 0 |
| 0158 | Daily Life | checking an important detail — daily routines | Ms Marcella | 1222 | 108 | 0 |
| 0159 | Learning | checking an important detail — school & learning | Mr Sylvester | 1288 | 108 | 0 |
| 0160 | Work | checking an important detail — workplace communication | Ms Philomena | 1251 | 108 | 0 |
| 0161 | Communication | checking an important detail — phone calls | Mr Corwin | 1257 | 108 | 0 |
| 0162 | Communication | checking an important detail — messages & digital communication | Ms Delphine | 1249 | 108 | 0 |

Total English learning words, Delivery #19: **11,371**.
Structural page estimate ≈ **36.9 pages** — inside the ~36-38 target,
so Delivery #19 is closed here. Do not add Lessons 0163-0169 to this
table; they open Delivery #20 (documented individually below).

Cross-lesson check ran against the entire book so far via
`build_delivery19.py`'s `WHOLE_BOOK` list — Lessons 0154-0159 needed 11
first-pass fixes (see below), and extending the delivery with Lessons
0160-0162 surfaced 12 more first-pass collisions, all short generic
reactions ("good, we still have plenty of time then.", "great, one
less thing to worry about.", "good to know, I will plan around that.")
colliding with much earlier lessons or with each other. All fixed by
rewording the later-appearing line to echo a specific detail from its
own answer; two rewordings introduced fresh accidental collisions on
the next pass and needed a further round of fixes. A final whole-book
pass found 0 remaining collisions. Result: **0 duplicates across the
whole book, 0001-0162.**
**Lesson learned:** confirms the "checking an important detail about
X" pattern's collision risk documented after Delivery #18 continues
across domains — the short "Good, [reaction]" and "Yes/No, [detail]."
lines need the "echo a specific detail" rule applied from the first
draft in every one of these lessons, not just the single-premise ones.
Also confirms that a reworded fix can itself introduce a NEW collision
with a different earlier lesson — always re-run the whole-book check
after every round of fixes, not just once.

## Per-lesson QC record — DELIVERY #20 (OPEN)

| Lesson | Domain | Scenario | Secondary character | EN words | Turns | Duplicate lines |
|---|---|---|---|---|---|---|
| 0163 | Personal Identity | where you live | Mr Tobias | 1179 | 108 | 0 |
| 0164 | Social Basics | saying thank you | Ms Arabella | 1355 | 108 | 0 |
| 0165 | Numbers and Time | today's date | Mr Jasper | 1269 | 108 | 0 |
| 0166 | Home | something you need at home | Ms Cecily | 1294 | 108 | 0 |
| 0167 | Family | a simple family relationship | Mr Lucian | 1482 | 108 | 0 |
| 0168 | Food | saying you are hungry or thirsty | Ms Miranda | 1225 | 108 | 0 |
| 0169 | Shopping | asking for help with shopping & payments | Mr Bertrand | 1272 | 108 | 0 |

Total English learning words, Delivery #20 so far: **9,076**.
Structural page estimate so far ≈ **28.7 pages** — under the ~36-38
target, so this delivery stays OPEN; Lessons from Block 0170-0179 will
be appended to it next via a rebuilt `build_delivery20.py`.

Cross-lesson check ran against the entire book so far via
`build_delivery20.py`'s `WHOLE_BOOK` list (Deliveries #1-#19 plus these
7 lessons) — 19 first-pass collisions found across Lessons 0164-0169,
mostly short generic reactions colliding with much earlier lessons.
All fixed by rewording the later-appearing line to echo a specific
detail from its own answer. Separately, a manual audit against the
cumulative names-used list (prompted by this round's fixes) found that
Lessons 0166, 0167, 0168, and 0169 had used the master workbook's
suggested secondary-character names directly (Grace, Henry, Anna,
David) without substituting a fresh name — all four names were already
used many lessons earlier and this was NOT caught by the automated
duplicate-line check, which has no visibility into character names.
Fixed via find-and-replace to Cecily, Lucian, Miranda, and Bertrand.
A final whole-book pass after all fixes found 0 remaining line
collisions. Result: **0 duplicates across the whole book, 0001-0169.**
**Lesson learned:** see the Status section note above — always
actively substitute a fresh secondary-character name for the master
workbook's suggestion, and manually check both speaker names in every
new lesson against the cumulative names-used list, since the automated
QC tooling only checks dialogue text, never character names.

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
