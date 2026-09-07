# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor
from lesson_builder import (
    add_title_block, add_lesson_header_table, add_blank_spacer,
    add_intro_paragraph, add_dialogue_line, qc_report, lesson_word_count,
    find_exact_duplicate_lines,
)
from lesson0002 import LESSON_0002
from lesson0003 import LESSON_0003
from lesson0004 import LESSON_0004
from lesson0005 import LESSON_0005

LESSONS_NEW = [LESSON_0002, LESSON_0003, LESSON_0004, LESSON_0005]

def cross_lesson_duplicate_check(all_lessons):
    seen = {}
    dups = []
    for lesson in all_lessons:
        for (speaker, en, vi) in lesson['turns']:
            key = en.strip().lower()
            if key in seen and seen[key] != lesson['lesson_id']:
                dups.append((key, seen[key], lesson['lesson_id']))
            else:
                seen[key] = lesson['lesson_id']
    return dups

def main():
    base_path = "lesson0001_approved.docx"
    doc = docx.Document(base_path)

    for idx, lesson in enumerate(LESSONS_NEW):
        doc.add_page_break()
        add_title_block(doc)
        add_lesson_header_table(doc, lesson['cefr'], lesson['lesson_id'], lesson['en_title'], lesson['vi_title'])
        add_blank_spacer(doc)
        add_intro_paragraph(doc, lesson['intro_en'], lesson['intro_vi'])
        for speaker, en, vi in lesson['turns']:
            add_dialogue_line(doc, speaker, en, vi)

    # Update footer to reflect combined lesson range
    sec = doc.sections[0]
    ftr = sec.footer
    p = ftr.paragraphs[0]
    # remove existing runs
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    r = p.add_run("EVERYDAY ENGLISH REFLEX  •  Lessons 0001–0005  •  page ")
    r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    r.font.size = Pt(8)
    from lesson_builder import add_page_number_field
    add_page_number_field(p)

    out_path = "EVERYDAY_ENGLISH_REFLEX_LESSONS_0001-0005.docx"
    doc.save(out_path)
    print("Saved:", out_path)

    # QC summary
    import docx as docx2
    d1 = docx2.Document(base_path)
    en_words_1 = 0
    import re
    turns_1 = 0
    speakers_1 = set()
    intro_words_1 = len(re.findall(r"[A-Za-z']+", re.split(r'\s{2,}', d1.paragraphs[3].text, maxsplit=1)[0]))
    for para in d1.paragraphs:
        t = para.text.strip()
        if not t or ':' not in t:
            continue
        m = re.match(r'^([A-Za-z .]+):\s*(.*)$', t)
        if not m:
            continue
        speakers_1.add(m.group(1).strip())
        rest = m.group(2)
        parts = re.split(r'\s{2,}', rest, maxsplit=1)
        en = parts[0].strip()
        turns_1 += 1
        en_words_1 += len(re.findall(r"[A-Za-z']+", en))
    en_words_1 += intro_words_1

    print("\n=== PER-LESSON QC ===")
    print(f"Lesson 0001 (approved, preserved): English words (incl. intro)={en_words_1}, turns={turns_1}, speakers={sorted(speakers_1)}")
    all_lessons_for_dup = LESSONS_NEW
    for lesson in LESSONS_NEW:
        r = qc_report(lesson)
        print(f"Lesson {r['lesson_id']}: English words={r['english_words']}, turns={r['turns']}, "
              f"speakers={sorted(r['speakers'])}, duplicate_lines={r['duplicate_lines']}")

    cross_dups = cross_lesson_duplicate_check(LESSONS_NEW)
    print("\nCross-lesson (0002-0005) duplicate English lines:", cross_dups)

    total_words = en_words_1 + sum(lesson_word_count(l) for l in LESSONS_NEW)
    print("\nTotal English learning words across 5 lessons:", total_words)

if __name__ == "__main__":
    main()
