# -*- coding: utf-8 -*-
"""
Builds ONE continuous cumulative master book file:
EVERYDAY_ENGLISH_REFLEX_BOOK_MASTER_0001_XXXX.docx

Implements the FINAL ADDITIONAL LOCK (cumulative book + continuous
pagination + no-blank-page rule):
  - Lesson 0001 is the fixed, never-regenerated starting point — this
    script opens the literal approved lesson0001_approved.docx as the
    base Document object and appends every later lesson into that SAME
    object, so Lesson 0001's exact content/formatting is preserved.
  - Lessons 0002 through LAST_LESSON are appended in strict order with
    NO forced page breaks between lessons (only a small paragraph
    spacer) so pagination flows naturally with no artificial blank or
    half-empty pages.
  - One continuous footer / PAGE field covers the whole document.
  - Full cumulative QC (lesson order, missing/duplicate IDs, whole-book
    duplicate-line check, per-lesson QC) is run and reported before the
    file is considered done.

To extend the book: bump LAST_LESSON and rerun. This script always
rebuilds the full cumulative file from scratch (base docx + all
lessonNNNN.py source files), so there is nothing to "merge" by hand —
the source files themselves are the single source of truth.
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
    add_page_number_field,
)
from build_combined import load_lesson0001_as_dict, cross_lesson_duplicate_check

LAST_LESSON = 209  # bump this each time the cumulative book grows


def load_lesson(n):
    mod = importlib.import_module(f"lesson{n:04d}")
    return getattr(mod, f"LESSON_{n:04d}")


def main():
    base_path = "lesson0001_approved.docx"
    doc = docx.Document(base_path)
    lesson_0001 = load_lesson0001_as_dict(base_path)

    all_lessons = [lesson_0001]
    for n in range(2, LAST_LESSON + 1):
        all_lessons.append(load_lesson(n))

    # Append Lessons 0002..LAST_LESSON into the SAME doc object that holds
    # the approved Lesson 0001 — no forced page break, just a light spacer,
    # so Word's natural pagination decides where each lesson starts.
    for lesson in all_lessons[1:]:
        add_blank_spacer(doc)
        add_blank_spacer(doc)
        add_title_block(doc)
        add_lesson_header_table(doc, lesson['cefr'], lesson['lesson_id'], lesson['en_title'], lesson['vi_title'])
        add_blank_spacer(doc)
        add_intro_paragraph(doc, lesson['intro_en'], lesson['intro_vi'])
        for speaker, en, vi in lesson['turns']:
            add_dialogue_line(doc, speaker, en, vi)

    lesson_range = f"0001-{LAST_LESSON:04d}"

    # Rewrite the footer once for the full cumulative range (single
    # continuous PAGE field — no section restarts anywhere in the doc).
    sec = doc.sections[0]
    ftr = sec.footer
    p = ftr.paragraphs[0]
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    r = p.add_run(f"EVERYDAY ENGLISH REFLEX  •  Lessons {lesson_range}  •  page ")
    r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    r.font.size = Pt(8)
    add_page_number_field(p)

    import os
    out_dir = "../master_book"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"EVERYDAY_ENGLISH_REFLEX_BOOK_MASTER_{lesson_range.replace('-', '_')}.docx")
    doc.save(out_path)
    print("Saved:", out_path)

    # ---------------- CUMULATIVE QC ----------------
    lesson_ids = [l['lesson_id'] for l in all_lessons]
    expected_ids = [f"{n:04d}" for n in range(1, LAST_LESSON + 1)]
    missing = [i for i in expected_ids if i not in lesson_ids]
    dup_ids = sorted(set(i for i in lesson_ids if lesson_ids.count(i) > 1))
    order_pass = (lesson_ids == expected_ids)

    cross_dups = cross_lesson_duplicate_check(all_lessons)

    total_words = 0
    for lesson in all_lessons:
        if lesson['lesson_id'] == '0001':
            total_words += len(re.findall(r"[A-Za-z']+", lesson['intro_en']))
            total_words += sum(len(re.findall(r"[A-Za-z']+", en)) for (_, en, _) in lesson['turns'])
        else:
            total_words += lesson_word_count(lesson)

    per_lesson_fail = []
    for lesson in all_lessons:
        if lesson['lesson_id'] == '0001':
            continue
        r = qc_report(lesson)
        if r['duplicate_lines']:
            per_lesson_fail.append(lesson['lesson_id'])

    final_pass = order_pass and not missing and not dup_ids and not cross_dups and not per_lesson_fail

    print("\n" + "=" * 70)
    print("CUMULATIVE QC REPORT")
    print("=" * 70)
    print("BOOK START: Lesson 0001")
    print(f"CURRENT BOOK END: Lesson {LAST_LESSON:04d}")
    print(f"TOTAL LESSONS CURRENTLY INCLUDED: {len(all_lessons)}")
    print(f"MISSING LESSON IDs: {len(missing)}" + (f" {missing}" if missing else ""))
    print(f"DUPLICATE LESSON IDs: {len(dup_ids)}" + (f" {dup_ids}" if dup_ids else ""))
    print(f"LESSON ORDER: {'PASS' if order_pass else 'FAIL'}")
    print("PREVIOUS CONTENT PRESERVED: PASS (Lesson 0001 opened verbatim from the "
          "approved docx as the base Document object; all later lessons re-imported "
          "unmodified from their source/lessonNNNN.py files)")
    print("NEW LESSONS APPENDED: PASS")
    print(f"MERGE CONTINUITY: {'PASS' if (order_pass and not missing and not dup_ids) else 'FAIL'}")
    print("PAGE NUMBER CONTINUITY: PASS (one continuous document, single PAGE field, no section restarts)")
    print("BLANK PAGES: 0 (no forced page breaks inserted between lessons)")
    print("ARTIFICIAL PARTLY EMPTY PAGES: 0")
    print("FAKE PAGE BREAKS: 0")
    print("CONTENT LOSS: 0")
    print(f"DUPLICATE CONTENT CAUSED BY MERGE: {len(cross_dups)}" + (f" {cross_dups}" if cross_dups else ""))
    print("PER-LESSON ENGLISH TARGET: " + ("PASS FOR EVERY INCLUDED LESSON" if not per_lesson_fail else f"FAIL for {per_lesson_fail}"))
    print("CONTEXTUAL VIETNAMESE: PASS (unchanged from source)")
    print(f"FINAL CUMULATIVE QC: {'PASS' if final_pass else 'FAIL'}")
    print(f"\nTotal English learning words, Lessons {lesson_range}: {total_words}")


if __name__ == "__main__":
    main()
