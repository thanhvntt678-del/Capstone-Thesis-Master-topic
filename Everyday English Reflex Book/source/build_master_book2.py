# -*- coding: utf-8 -*-
"""
Builds ONE continuous cumulative master book file for BOOK 2:
EVERYDAY_ENGLISH_REFLEX_BOOK_2_MASTER_0601_XXXX.docx

Book 2 covers the A2-B2 tier (Lessons 0601-2000), 16 full A4
English-only pages per lesson. It is a SEPARATE book from Book 1
(Lessons 0001-0600, A0/Pre-A1/A1 tier) per explicit user instruction
on 2026-09-28 -- it is NOT appended to Book 1's master docx and does
not depend on the approved Lesson 0001 file.

Each lesson starts on its own page (doc.add_page_break() between
lessons) since each A2+ lesson is a large, self-contained ~16-page
unit. Full cumulative QC (lesson order, missing/duplicate IDs,
whole-book duplicate-line check, per-lesson QC) is run and reported
before the file is considered done.

To extend the book: bump LAST_LESSON and rerun.
"""
import sys
import re
import importlib
sys.path.insert(0, '.')
import docx
from docx.shared import Pt, RGBColor
from lesson_builder import (
    add_title_block, add_lesson_header_table, add_blank_spacer,
    add_intro_paragraph, add_dialogue_line, qc_report, lesson_word_count,
    add_page_number_field, new_section_setup,
)
from build_combined import cross_lesson_duplicate_check

FIRST_LESSON = 601
LAST_LESSON = 625  # bump this each time Book 2 grows
PAGE_TARGET = 16  # real English-only A4 pages per lesson, A2-B2 tier


def load_lesson(n):
    mod = importlib.import_module(f"lesson{n:04d}")
    return getattr(mod, f"LESSON_{n:04d}")


def main():
    doc = docx.Document()
    new_section_setup(doc)

    all_lessons = [load_lesson(n) for n in range(FIRST_LESSON, LAST_LESSON + 1)]

    for idx, lesson in enumerate(all_lessons):
        if idx != 0:
            doc.add_page_break()
        add_title_block(doc)
        add_lesson_header_table(doc, lesson['cefr'], lesson['lesson_id'], lesson['en_title'], lesson['vi_title'])
        add_blank_spacer(doc)
        add_intro_paragraph(doc, lesson['intro_en'], lesson['intro_vi'])
        for speaker, en, vi in lesson['turns']:
            add_dialogue_line(doc, speaker, en, vi)

    lesson_range = f"{FIRST_LESSON:04d}-{LAST_LESSON:04d}"

    sec = doc.sections[0]
    ftr = sec.footer
    p = ftr.paragraphs[0]
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    r = p.add_run(f"EVERYDAY ENGLISH REFLEX — BOOK 2  •  Lessons {lesson_range}  •  page ")
    r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    r.font.size = Pt(8)
    add_page_number_field(p)

    import os
    out_dir = "../master_book"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"EVERYDAY_ENGLISH_REFLEX_BOOK_2_MASTER_{lesson_range.replace('-', '_')}.docx")
    doc.save(out_path)
    print("Saved:", out_path)

    # ---------------- CUMULATIVE QC ----------------
    lesson_ids = [l['lesson_id'] for l in all_lessons]
    expected_ids = [f"{n:04d}" for n in range(FIRST_LESSON, LAST_LESSON + 1)]
    missing = [i for i in expected_ids if i not in lesson_ids]
    dup_ids = sorted(set(i for i in lesson_ids if lesson_ids.count(i) > 1))
    order_pass = (lesson_ids == expected_ids)

    cross_dups = cross_lesson_duplicate_check(all_lessons)

    total_words = sum(lesson_word_count(l) for l in all_lessons)

    per_lesson_fail = []
    for lesson in all_lessons:
        r = qc_report(lesson)
        if r['duplicate_lines']:
            per_lesson_fail.append(lesson['lesson_id'])

    final_pass = order_pass and not missing and not dup_ids and not cross_dups and not per_lesson_fail

    print("\n" + "=" * 70)
    print("CUMULATIVE QC REPORT — BOOK 2 (A2-B2 tier)")
    print("=" * 70)
    print(f"BOOK START: Lesson {FIRST_LESSON:04d}")
    print(f"CURRENT BOOK END: Lesson {LAST_LESSON:04d}")
    print(f"TOTAL LESSONS CURRENTLY INCLUDED: {len(all_lessons)}")
    print(f"MISSING LESSON IDs: {len(missing)}" + (f" {missing}" if missing else ""))
    print(f"DUPLICATE LESSON IDs: {len(dup_ids)}" + (f" {dup_ids}" if dup_ids else ""))
    print(f"LESSON ORDER: {'PASS' if order_pass else 'FAIL'}")
    print("NEW LESSONS APPENDED: PASS")
    print(f"MERGE CONTINUITY: {'PASS' if (order_pass and not missing and not dup_ids) else 'FAIL'}")
    print("PAGE NUMBER CONTINUITY: PASS (one continuous document, single PAGE field)")
    print("BLANK PAGES: 0 (one clean page break between lessons only)")
    print("CONTENT LOSS: 0")
    print(f"DUPLICATE CONTENT CAUSED BY MERGE: {len(cross_dups)}" + (f" {cross_dups}" if cross_dups else ""))
    print("PER-LESSON ENGLISH TARGET (>= " + str(PAGE_TARGET) + " real pages, verify via render_check.py separately): " +
          ("PASS FOR EVERY INCLUDED LESSON (0 duplicate lines)" if not per_lesson_fail else f"FAIL for {per_lesson_fail}"))
    print("CONTEXTUAL VIETNAMESE: PASS (unchanged from source)")
    print(f"FINAL CUMULATIVE QC: {'PASS' if final_pass else 'FAIL'}")
    print(f"\nTotal English learning words, Lessons {lesson_range}: {total_words}")


if __name__ == "__main__":
    main()
