import re
import docx
from docx.shared import Pt, Emu, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

A4_WIDTH = Emu(7560310)
A4_HEIGHT = Emu(10692130)
MARGIN_LR = Emu(720090)
MARGIN_TB = Emu(647700)
HEADER_DIST = Emu(457200)
FOOTER_DIST = Emu(457200)

NAVY = RGBColor(0x1F, 0x38, 0x64)
GREY_SUB = RGBColor(0x44, 0x44, 0x44)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHTBLUE = "D9E2F3"
DARKNAVY = "1F3864"
DARKGREY = "333333"


def set_cell_shading(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)


def add_page_number_field(paragraph):
    run = paragraph.add_run()
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = 'PAGE'
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set(qn('w:fldCharType'), 'end')
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)


def new_section_setup(doc):
    sec = doc.sections[0]
    sec.page_width = A4_WIDTH
    sec.page_height = A4_HEIGHT
    sec.left_margin = MARGIN_LR
    sec.right_margin = MARGIN_LR
    sec.top_margin = MARGIN_TB
    sec.bottom_margin = MARGIN_TB
    sec.header_distance = HEADER_DIST
    sec.footer_distance = FOOTER_DIST
    return sec


def add_title_block(doc):
    p0 = doc.add_paragraph()
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0 = p0.add_run("EVERYDAY ENGLISH REFLEX")
    r0.font.name = "Arial"
    r0.font.size = Pt(12)
    r0.font.bold = True
    r0.font.color.rgb = NAVY

    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_after = Pt(8)
    r1 = p1.add_run("GIAO TIẾP PHẢN XẠ THỰC TẾ")
    r1.font.name = "Arial"
    r1.font.size = Pt(9.5)
    r1.font.italic = True
    r1.font.color.rgb = GREY_SUB


def add_lesson_header_table(doc, cefr, lesson_id, en_title, vi_title):
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_ALIGN_PARAGRAPH.CENTER
    table.autofit = False
    col0_w = Emu(1151890)
    col1_w = Emu(4968240)
    table.columns[0].width = col0_w
    table.columns[1].width = col1_w
    cell0, cell1 = table.rows[0].cells
    cell0.width = col0_w
    cell1.width = col1_w

    set_cell_shading(cell0, DARKNAVY)
    p = cell0.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(cefr)
    r.font.name = "Arial"; r.font.size = Pt(12); r.font.bold = True; r.font.color.rgb = WHITE
    p2 = cell0.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run(f"LESSON {lesson_id}")
    r2.font.name = "Arial"; r2.font.size = Pt(8); r2.font.color.rgb = WHITE

    set_cell_shading(cell1, LIGHTBLUE)
    p3 = cell1.paragraphs[0]
    r3 = p3.add_run(en_title)
    r3.font.name = "Arial"; r3.font.size = Pt(15); r3.font.bold = True
    r3.font.color.rgb = NAVY
    p4 = cell1.add_paragraph()
    r4 = p4.add_run(vi_title)
    r4.font.name = "Arial"; r4.font.size = Pt(11); r4.font.italic = True
    r4.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

    return table


def add_blank_spacer(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)


def add_intro_paragraph(doc, en_text, vi_text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    r1 = p.add_run(en_text)
    r1.font.name = "Calibri"; r1.font.size = Pt(9.5); r1.font.italic = True
    r2 = p.add_run("  " + vi_text)
    r2.font.name = "Calibri"; r2.font.size = Pt(9.5); r2.font.italic = True


def add_dialogue_line(doc, speaker, en_text, vi_text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.line_spacing = 1.3
    r_sp = p.add_run(f"{speaker}: ")
    r_sp.font.name = "Calibri"; r_sp.font.size = Pt(11); r_sp.font.bold = True
    r_en = p.add_run(en_text + "  ")
    r_en.font.name = "Calibri"; r_en.font.size = Pt(11)
    r_vi = p.add_run(vi_text)
    r_vi.font.name = "Calibri"; r_vi.font.size = Pt(11); r_vi.font.italic = True


def add_footer(doc, domain_label):
    sec = doc.sections[0]
    ftr = sec.footer
    p = ftr.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(f"EVERYDAY ENGLISH REFLEX  •  {domain_label}  •  page ")
    r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    r.font.size = Pt(8)
    add_page_number_field(p)


def build_single_lesson_doc(lesson):
    """lesson: dict with keys cefr, lesson_id, en_title, vi_title, domain,
    intro_en, intro_vi, turns: list of (speaker, en, vi)"""
    doc = docx.Document()
    new_section_setup(doc)
    add_title_block(doc)
    add_lesson_header_table(doc, lesson['cefr'], lesson['lesson_id'], lesson['en_title'], lesson['vi_title'])
    add_blank_spacer(doc)
    add_intro_paragraph(doc, lesson['intro_en'], lesson['intro_vi'])
    for speaker, en, vi in lesson['turns']:
        add_dialogue_line(doc, speaker, en, vi)
    add_footer(doc, lesson['domain'])
    return doc


def build_combined_doc(lessons):
    doc = docx.Document()
    new_section_setup(doc)
    for idx, lesson in enumerate(lessons):
        add_title_block(doc)
        add_lesson_header_table(doc, lesson['cefr'], lesson['lesson_id'], lesson['en_title'], lesson['vi_title'])
        add_blank_spacer(doc)
        add_intro_paragraph(doc, lesson['intro_en'], lesson['intro_vi'])
        for speaker, en, vi in lesson['turns']:
            add_dialogue_line(doc, speaker, en, vi)
        if idx != len(lessons) - 1:
            doc.add_page_break()
    add_footer(doc, "Master Book 0001–2000")
    return doc


def count_english_words(en_text):
    return len(re.findall(r"[A-Za-z']+", en_text))


def lesson_word_count(lesson):
    total = count_english_words(lesson['intro_en'])
    for speaker, en, vi in lesson['turns']:
        total += count_english_words(en)
    return total


def find_exact_duplicate_sentences(lesson):
    """Return list of English sentences (normalized) that appear more than once."""
    sentences = []
    texts = [lesson['intro_en']] + [en for (_, en, _) in lesson['turns']]
    for t in texts:
        for s in re.split(r'(?<=[.!?])\s+', t.strip()):
            s = s.strip()
            if s:
                norm = re.sub(r'\s+', ' ', s.lower()).strip('.! ?')
                sentences.append(norm)
    seen = {}
    dups = []
    for s in sentences:
        seen[s] = seen.get(s, 0) + 1
    for s, c in seen.items():
        if c > 1:
            dups.append((s, c))
    return dups


def find_exact_duplicate_lines(lesson):
    lines = [en.strip().lower() for (_, en, _) in lesson['turns']]
    seen = {}
    for l in lines:
        seen[l] = seen.get(l, 0) + 1
    return [(l, c) for l, c in seen.items() if c > 1]


def qc_report(lesson):
    wc = lesson_word_count(lesson)
    dup_sent = find_exact_duplicate_sentences(lesson)
    dup_lines = find_exact_duplicate_lines(lesson)
    turns = len(lesson['turns'])
    speakers = set(s for (s, _, _) in lesson['turns'])
    return {
        'lesson_id': lesson['lesson_id'],
        'english_words': wc,
        'turns': turns,
        'speakers': speakers,
        'duplicate_sentences': dup_sent,
        'duplicate_lines': dup_lines,
    }
