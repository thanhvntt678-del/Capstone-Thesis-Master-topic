# PRACTICAL EVERYDAY ENGLISH — SÁCH GIAO TIẾP PHẢN XẠ THỰC TẾ

Foundation → A1 → A2 → B1 → B1+ → B2 bilingual (EN/VI) communicative
English book.

## ACTIVE SYSTEM: Master V3 (Situation 0001–2000)
Governing spec: **`PROJECT_RULES_V3.md`** (supersedes `PROJECT_RULES.md`
where they conflict). Current scope is **book production only** — no
Excel/Python/TTS/MP4 at this stage. Workflow is **one Situation at a time**
with an explicit NEXT-lock: work stops completely after each Situation is
delivered and QC-reported, and only resumes when the user sends `NEXT`.

- `book/situations/situation_NNNN.json` — one file per Situation (source of
  truth). Character system: **Ms Lan** (fixed main character) + exactly one
  other named character per Situation. Full-form English (no contractions).
- `scripts/build_book_docx.py` — renders `book/manuscript/
  PRACTICAL_EVERYDAY_ENGLISH_BOOK.docx` (inline bilingual layout: bold name
  + English + Vietnamese on the same visual row, no labels, no images).
- `scripts/compute_situation_stats.py <situation_file>` — per-Situation QC:
  exact English word count, contraction check, exact-duplicate check,
  speaker check.
- `PROGRESS.json` — `NEXT_SITUATION_TO_WRITE` / `NEXT_SITUATION_SOURCE_CODE`
  / `NEXT_SITUATION_STATUS` track exactly where this stands.

### To continue this project in a new session
1. Read `PROJECT_RULES_V3.md` in full — literal governing spec.
2. Check `PROGRESS.json` → `NEXT_SITUATION_STATUS`. If it is
   `WAITING_FOR_NEXT_COMMAND`, **do not write the next Situation** — wait
   for the user to send `NEXT` (Rule: NEXT LOCK).
3. Once `NEXT` is received: look up `NEXT_SITUATION_SOURCE_CODE` in
   `source_reference/DGE_video_index_001_401.csv` for the topic/CEFR (once
   past DGE0401, write original content per the Foundation→B2 roadmap).
4. Write `book/situations/situation_NNNN.json`, run
   `compute_situation_stats.py`, run `build_book_docx.py`, self-QC against
   every field in the V3 QC report template, fix any failure, re-render,
   re-QC, then deliver with the exact QC report format and STOP.

## Deprecated (pre-V3) system — kept for audit trail only
`data/lessons/lesson_001.json`–`lesson_020.json`, `PROJECT_RULES.md`, and
the Excel/DOCX scripts under the old "Lesson 001–401" numbering used
Person A/Person B speakers and allowed contractions. Superseded by Master
V3 (wrong character system, wrong numbering, wrong layout) — not deleted,
not to be extended further.

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
