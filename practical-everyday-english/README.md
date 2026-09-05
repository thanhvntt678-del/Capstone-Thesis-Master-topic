# EVERYDAY ENGLISH REFLEX — GIAO TIẾP PHẢN XẠ THỰC TẾ

A0/Pre-A1 → A1 → A2 → B1 → B1+ → B2 bilingual (EN/VI) communicative
English book.

## ACTIVE SYSTEM: RESTART FINAL (Lesson 0001–2000)
Governing spec: **`PROJECT_RULES_RESTART.md`** — the sole authority now,
superseding both `PROJECT_RULES.md` (old Lesson 001–401 / Person A-B) and
`PROJECT_RULES_V3.md` (Situation 0001–2000 / Ms Lan). The four old
DGE001–401 source files are dropped entirely; curriculum is driven only by
`source_reference/MASTER_2000_LESSONS.csv` (2000 locked rows: Lesson ID,
CEFR, Major Domain, Scenario, English/Vietnamese titles, Communication
Goal, word/page targets). Scope is **book production only** (no
Excel/Python/TTS/MP4 at this stage). Workflow is **one Lesson at a time**
with an explicit NEXT-lock: stop completely after each Lesson is delivered
and QC-reported, resume only when the user sends `NEXT`.

- `restart/lessons/lesson_NNNN.json` — one file per Lesson (source of
  truth). **Ms Lan** (fixed main character) + exactly one other named
  character per Lesson. Full-form English (no contractions).
- `scripts/build_restart_docx.py` — renders `restart/manuscript/
  EVERYDAY_ENGLISH_REFLEX_BOOK.docx` (inline bilingual layout: bold name +
  English + Vietnamese on the same visual row, no labels, no images).
- `scripts/compute_lesson_stats.py <lesson_file>` — per-Lesson QC: exact
  English word count, contraction check, exact-duplicate check, speaker
  alternation check.
- `PROGRESS.json` — `NEXT_LESSON_TO_WRITE_RESTART` /
  `NEXT_LESSON_STATUS_RESTART` track exactly where this stands.

### To continue this project in a new session
1. Read `PROJECT_RULES_RESTART.md` in full — literal governing spec.
2. Check `PROGRESS.json` → `NEXT_LESSON_STATUS_RESTART`. If it is
   `WAITING_FOR_NEXT_COMMAND`, **do not write the next Lesson** — wait for
   the user to send `NEXT` (NEXT LOCK).
3. Once `NEXT` is received: look up the next Lesson ID's exact row in
   `source_reference/MASTER_2000_LESSONS.csv` for its locked CEFR level,
   Major Domain, Scenario, titles, Communication Goal, and word/page
   targets — never substitute a different topic.
4. Write `restart/lessons/lesson_NNNN.json`, run
   `compute_lesson_stats.py`, run `build_restart_docx.py`, self-QC against
   every field in the restart QC report template (`04_QC_REPORT` sheet),
   fix any failure, re-render, re-QC, then deliver with the exact QC
   report format and STOP.

## Superseded systems — kept for audit trail only, not extended further
- `data/lessons/lesson_001.json`–`lesson_020.json` + `PROJECT_RULES.md`:
  original "Lesson 001–401" system, Person A/Person B, contractions
  allowed.
- `book/situations/situation_0001.json` + `PROJECT_RULES_V3.md`: "Situation
  0001–2000" system built on the old DGE001–401 source content.
Both are superseded by the RESTART FINAL system above.

## Layout
- `data/lessons/lesson_NNN.json` — one file per lesson. Source of truth.
  Schema: `lesson_id, source_code, major_topic, major_topic_vi, situation_id,
  situation_title_en, situation_title_vi, cefr, context_note_en,
  context_note_vi, turns[]`. Each turn: `turn_order, speaker (Person A|
  Person B only), english, vietnamese, is_learning_text, mp4_part`.
- `source_reference/` — original DGE0001–0401 workbooks' VIDEO INDEX
  (topic/CEFR sequencing, kept) and raw DIALOGUE LINES dumps (drill script,
  superseded — kept only for audit trail, not reused as book content).
- `scripts/compute_stats.py` — TOTAL_ENGLISH_WORDS / ESTIMATED_ENGLISH_A4_PAGES
  across all written lessons (English text only, per Rule 15).
- `scripts/export_excel.py` — builds `export/PRACTICAL_EVERYDAY_ENGLISH_MASTER.xlsx`
  (the Python-ready master, exact schema from Rule 6/18).
- `scripts/build_docx.py` — builds `manuscript/PRACTICAL_EVERYDAY_ENGLISH.docx`
  (designed A4 manuscript: navy header, CEFR badge, section bars, dialogue
  table, footer, auto page numbers — Rule 16).

## To continue this project in a new session
1. Read `PROJECT_RULES.md` in full — it is the complete, literal governing
   spec (do not re-derive or renegotiate it).
2. Read `PROGRESS.json` for `NEXT_LESSON_TO_WRITE` / `NEXT_SOURCE_CODE`.
3. Look up that source code in `source_reference/DGE_video_index_001_401.csv`
   for the next topic title, module, and CEFR level (once past DGE0401,
   there is no more source — continue writing original situations at
   ascending CEFR per Rule 14, still meeting the life-domain coverage in
   Rule 13).
4. Write `data/lessons/lesson_NNN.json` for the next lesson(s) as genuine
   Person A / Person B communicative dialogue (never reuse the drill text
   in `source_reference/*_dialogue.csv` — it fails the naturalness rules).
5. Re-run `scripts/compute_stats.py`, `scripts/export_excel.py`,
   `scripts/build_docx.py`; update `PROGRESS.json`; commit.
6. Keep going without asking whether to continue (Rule 20) — stop only to
   checkpoint progress, not to ask permission.
