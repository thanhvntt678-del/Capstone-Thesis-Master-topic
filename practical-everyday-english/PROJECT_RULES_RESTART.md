# RESTART FINAL — governing spec (supersedes PROJECT_RULES.md AND PROJECT_RULES_V3.md)

Source: `CLAUDE_BOOK_MASTER_2000_LESSONS_PREA1_TO_B2_RESTART_FINAL.xlsx` +
its "FINAL ABSOLUTE COMMAND" chat message. **This is the sole authority now.**

## Full reset — old DGE001–401 files are dropped entirely
Do not read, reuse, repair, or continue the four old DGE001–401 source
files, and do not continue from the old "Situation 401" point. Restart
completely from **Lesson 0001**, driven only by sheet
`02_MASTER_2000_LESSONS` in the new master workbook (2000 rows, saved at
`source_reference/MASTER_2000_LESSONS.csv`).

## Numbering: Lesson 0001 → 2000 (level-locked, fixed)
- 0001–0250: A0 / Pre-A1 (real CEFR label: Pre-A1; "A0" is a friendly
  nickname only)
- 0251–0600: A1
- 0601–1000: A2
- 1001–1400: B1
- 1401–1700: B1+
- 1701–2000: B2

No skipping, merging, renumbering, or inventing a different curriculum.
Every Lesson must follow its **exact locked master row**: Lesson ID, CEFR
Level, Major Domain, Scenario, English Lesson Title, Vietnamese Lesson
Title, Primary Communication Goal, EN Word Target, Page Target. Never
substitute a different title/scenario, never write a dialogue that doesn't
achieve that row's Communication Goal.

## Pre-A1 must be genuinely beginner (hard lock)
Lessons 0001–0250 must not fake beginner level while writing A1/A2-level
dialogue. Progression inside Pre-A1: recognising/saying your name → asking
someone's name → spelling → greetings → yes/no → numbers → phone numbers →
age → country/city → simple personal info → dates/days/time → basic
objects → family → food/drink → immediate needs → simple requests → asking
for repetition → saying you don't understand → very simple real-life
exchanges. No workplace discussions, negotiation, complex problem-solving,
or long storytelling in Lesson 0001.

## Length is an editorial target, per level (not a CEFR rule, not a quota)
| Level | EN words | Actual bilingual A4 pages |
|---|---|---|
| Pre-A1/A0 | 180–260 | 2–3 |
| A1 | 260–380 | ~3 |
| A2 | 380–520 | 3–4 |
| B1 | 520–700 | ~4 |
| B1+ | 650–850 | 4–5 |
| B2 | 800–1000 | ~5 |

Priority order when they conflict: **CEFR appropriateness →
communicative completeness → naturalness → learning value → word/page
target.** Never pad (duplicate/near-duplicate/filler greetings-closings/
same skeleton with a new name or number) to hit a number. Actual page
count may naturally vary from the target — that is allowed, not a defect,
per the QC template itself ("Target range unless natural content justifies
variation").

## Characters, English, Vietnamese, layout, no-images/vocab/grammar
Same hard rules as the previous Master V3: **Ms Lan** fixed main character
+ exactly one other named Mr/Ms character per Lesson (never Person A/B,
Speaker A/B, "Customer"/"Staff" without a name); exactly 2 active speakers;
full-form English only (no contractions), still natural — not stiff;
Vietnamese translated for situation/meaning/tone/relationship, never
word-for-word; inline layout `Name: English.  Vietnamese.` on one visual
row when width permits, natural wrap only, no `English:`/`Tiếng Việt:`/
`Vietnamese:` labels, no fake turns; zero images/placeholders; zero
Vocabulary list; zero standalone Grammar lecture; zero blank/near-blank
pages; zero page-count manipulation (no oversized/tiny fonts, no spacing
tricks, no hidden/clipped/truncated text).

## Workflow — ONE Lesson at a time, then STOP (NEXT LOCK, absolute)
`READ EXACT MASTER ROW → UNDERSTAND CEFR/SCENARIO/GOAL → WRITE → EDIT →
FORMAT → RENDER → COUNT ENGLISH WORDS → COUNT ACTUAL BILINGUAL PAGES →
ENGLISH QC → VIETNAMESE QC → CEFR QC → DIALOGUE LOGIC QC → CHARACTER QC →
DUPLICATION QC → PAGE QC → PUBLICATION QC → SELF-CORRECT EVERY FAILURE →
RENDER AGAIN → RECOUNT → FINAL QC → EXPORT BOOK FILE → REPORT → STOP.`
Never deliver a failing Lesson. After FINAL QC = PASS, export + report, then
**stop completely** — no drafting, no preparing, no auto-continuing the
next Lesson. Resume only when the user sends `NEXT`.

## QC report format (exact fields, from sheet `04_QC_REPORT`)
Lesson ID/Title; CEFR; Main Character; Secondary Speaker; Active Speakers;
English Words; Actual Bilingual Pages; English Spelling/Grammar/Syntax;
English Collocation/Register/Naturalness; CEFR Appropriateness; Contextual
Vietnamese; Word-for-word Translation Errors; English-shaped Vietnamese;
Meaning Loss/Addition; Turn-to-turn Logic; Exact Duplicate English
Sentences; Artificial Padding; Images/Placeholders; Vocabulary/Grammar
Lecture; Blank/Near-blank Pages; Language Labels; Publication Layout;
FINAL QC; STATUS. **Note: this report format has no "Topic Mastery" field**
— unlike the earlier V3 Situation system, this restart's curriculum is
locked row-by-row with no flexible "continue same topic" gating mentioned
anywhere in the new master.

## LEVEL / CEFR AUTHORITY — ABSOLUTE LOCK (added after Lesson 0001/0002 correction)
Three sources, three distinct roles — never blur them:
1. **Council of Europe – CEFR Companion Volume + CEFR Descriptors** = the
   PRIMARY authority for level (Pre-A1/A0 → A1 → A2 → B1 → B2).
2. **Cambridge English Pre A1 Starters** = secondary reference only, to
   calibrate how simple Pre-A1 should read — never copy its child-learner
   content/characters into this adult book.
3. **Cambridge Dictionary / English–Vietnamese** = only for checking
   meaning, usage, collocation, and register, and for verifying Vietnamese
   sense — never used to decide CEFR level, and its machine-translation
   output is never copied as the final Vietnamese (see the translation
   pipeline below).

For Lessons 0001–0250: if content exceeds real Pre-A1 ability per CEFR,
REWRITE it, even if the English is grammatically correct. **CEFR LEVEL
ACCURACY > WORD COUNT > PAGE TARGET.** Never raise difficulty just to fill
2–3 pages.

Reference sources named by the user: CEFR Companion Volume
(coe.int/en/web/common-european-framework-reference-languages/cefr-companion-volume-and-its-language-versions),
CEFR Descriptors
(coe.int/en/web/common-european-framework-reference-languages/cefr-descriptors),
Cambridge Pre A1 Starters
(cambridgeenglish.org/exams-and-tests/qualifications/young-learners/paper/starters/format),
Cambridge Dictionary English–Vietnamese (dictionary.cambridge.org/vi/translate).
**Environment note:** `coe.int`, `cambridgeenglish.org`, and
`dictionary.cambridge.org` are all blocked by this sandbox's network
egress proxy — confirmed by direct fetch attempts, all returning
`EGRESS_BLOCKED`. Live lookups are not possible from this session; level
and translation judgement calls rely on trained knowledge of these
standards instead, applied with the same discipline (err toward simpler,
narrower scope; never let word/page targets justify raising difficulty).

## Vietnamese translation pipeline (mandatory per turn)
STEP 1 understand the exact English meaning → STEP 2 identify who is
speaking to whom → STEP 3 identify the real-life situation → STEP 4
identify communicative intention → STEP 5 identify politeness/register →
STEP 6 determine natural Vietnamese pronouns from the relationship and
situation → STEP 7 write what a Vietnamese person would naturally say in
the SAME situation. English is written and verified as natural English
FIRST, independently — never write Vietnamese first and back-translate
into English. After drafting, apply the **naturalness test**: hide the
English, read only the Vietnamese, and ask "would a Vietnamese person
really say this in this exact situation?" If no/awkward/translated-sounding
→ rewrite.

## Rendering-environment note (carried over, still true)
LibreOffice's `--convert-to pdf` fails to load any source file in this
sandbox (confirmed on a blank test document) — an environment limitation,
not a document defect. "Actual Bilingual Pages" is reported as a manual
layout estimate (wrapped-line count at the actual font/margins/line-height
used in the .docx → content height → pages), explicitly flagged as an
estimate rather than a verified render, until a working renderer is
available.

## Relationship to earlier work in this repo
- `data/lessons/` (old Lesson 001–401, Person A/B) — superseded, not
  deleted, not extended.
- `book/situations/` (Master V3, Situation 0001–2000) — also superseded
  by this full reset; Situation 0001 (DGE0001-based) is dropped, not
  carried forward, per this restart's explicit instruction to ignore the
  old DGE-sourced content entirely.
- **Active system now:** `restart/lessons/lesson_NNNN.json` →
  `scripts/build_restart_docx.py` →
  `restart/manuscript/EVERYDAY_ENGLISH_REFLEX_BOOK.docx`, driven strictly
  by `source_reference/MASTER_2000_LESSONS.csv`.
