# PRACTICAL EVERYDAY ENGLISH — TIẾNG ANH GIAO TIẾP THỰC CHIẾN

Zero → A1 → A2 → B1 → B2 communicative English book, bilingual (EN/VI),
Python/Excel/TTS/MP4 pipeline-ready. Governing spec: `PROJECT_RULES.md`.
Current status/checkpoint: `PROGRESS.json`.

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
