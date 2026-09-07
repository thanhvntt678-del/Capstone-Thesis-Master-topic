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
from lesson0006 import LESSON_0006

LESSONS_NEW = [LESSON_0002, LESSON_0003, LESSON_0004, LESSON_0005, LESSON_0006]

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

def load_lesson0001_as_dict(base_path):
    """Parse the approved Lesson 0001 docx into the same {lesson_id, turns:[...]} shape
    used by every other lesson, so it can go through the same QC/dup-check functions."""
    import re
    d = docx.Document(base_path)
    turns = []
    speakers = set()
    for para in d.paragraphs:
        t = para.text.strip()
        if not t or ':' not in t:
            continue
        m = re.match(r'^([A-Za-z .]+):\s*(.*)$', t)
        if not m:
            continue
        speaker = m.group(1).strip()
        parts = re.split(r'\s{2,}', m.group(2), maxsplit=1)
        en = parts[0].strip()
        vi = parts[1].strip() if len(parts) > 1 else ''
        speakers.add(speaker)
        turns.append((speaker, en, vi))
    intro_en = re.split(r'\s{2,}', d.paragraphs[3].text, maxsplit=1)[0]
    return {
        'lesson_id': '0001',
        'intro_en': intro_en,
        'turns': turns,
    }

def main():
    base_path = "lesson0001_approved.docx"
    doc = docx.Document(base_path)
    lesson_0001 = load_lesson0001_as_dict(base_path)
    ALL_LESSONS = [lesson_0001] + LESSONS_NEW
    lesson_range = f"{ALL_LESSONS[0]['lesson_id']}-{ALL_LESSONS[-1]['lesson_id']}"

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
    r = p.add_run(f"EVERYDAY ENGLISH REFLEX  •  Lessons {lesson_range}  •  page ")
    r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    r.font.size = Pt(8)
    from lesson_builder import add_page_number_field
    add_page_number_field(p)

    out_path = f"EVERYDAY_ENGLISH_REFLEX_LESSONS_{lesson_range}.docx"
    doc.save(out_path)
    print("Saved:", out_path)

    # QC summary (Lesson 0001 uses its own word/turn count since it has no
    # separately-tracked 'english_words'/'turns' fields the way new lessons do)
    print("\n=== PER-LESSON QC ===")
    for lesson in ALL_LESSONS:
        if lesson['lesson_id'] == '0001':
            words = len(__import__('re').findall(r"[A-Za-z']+", lesson['intro_en']))
            words += sum(len(__import__('re').findall(r"[A-Za-z']+", en)) for (_, en, _) in lesson['turns'])
            speakers = sorted(set(sp for (sp, _, _) in lesson['turns']))
            dups = find_exact_duplicate_lines(lesson)
            print(f"Lesson 0001 (approved, preserved): English words (incl. intro)={words}, "
                  f"turns={len(lesson['turns'])}, speakers={speakers}, duplicate_lines={dups}")
        else:
            r = qc_report(lesson)
            print(f"Lesson {r['lesson_id']}: English words={r['english_words']}, turns={r['turns']}, "
                  f"speakers={sorted(r['speakers'])}, duplicate_lines={r['duplicate_lines']}")

    cross_dups = cross_lesson_duplicate_check(ALL_LESSONS)
    print(f"\nCross-lesson duplicate English lines (0001 vs all new lessons, and among new lessons): {cross_dups}")

    total_words = 0
    for lesson in ALL_LESSONS:
        if lesson['lesson_id'] == '0001':
            total_words += len(__import__('re').findall(r"[A-Za-z']+", lesson['intro_en']))
            total_words += sum(len(__import__('re').findall(r"[A-Za-z']+", en)) for (_, en, _) in lesson['turns'])
        else:
            total_words += lesson_word_count(lesson)
    print(f"\nTotal English learning words across Lessons {lesson_range}:", total_words)

if __name__ == "__main__":
    main()
