# -*- coding: utf-8 -*-
"""Real (not estimated) English-only A4 page count for a single lesson,
via headless Chromium print-to-pdf — used to verify the locked A0/Pre-A1
target of >=5 English-only A4 pages per lesson.

Usage:
    python3 render_check.py 0170

Requires:
  - fonts-crosextra-carlito installed (exact Calibri metric clone; without
    it, results will be inaccurate — check with `fc-list | grep -i carlito`
    and `apt-get install -y fonts-crosextra-carlito` if missing)
  - /opt/pw-browsers/chromium-1194/chrome-linux/chrome (Playwright's
    pre-installed Chromium in this environment)

This performs REAL layout/pagination via an actual browser engine, not a
word-count or paragraph-count heuristic. Calibrated against the approved
Lesson 0001, which renders to exactly 5 pages with this exact CSS.
"""
import sys
import os
import html
import re
import subprocess
import importlib

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
TMP_DIR = "/tmp/render_check"

PAGE_CSS = """
@page { size: 210mm 297mm; margin: 18mm 20mm; }
* { box-sizing: border-box; }
body { margin: 0; font-family: "Liberation Sans", Arial, sans-serif; }
.title { text-align:center; font-weight:bold; font-size:12pt; color:#1F3864; margin:0; }
.subtitle { text-align:center; font-style:italic; font-size:9.5pt; color:#444444; margin:0 0 8pt 0; }
table.hdr { border-collapse:collapse; width:100%; margin: 4pt 0; }
table.hdr td { vertical-align:middle; padding:4pt 6pt; }
td.cefr { background:#1F3864; color:#fff; text-align:center; width:22%; }
td.cefr .lvl { font-size:12pt; font-weight:bold; }
td.cefr .lid { font-size:8pt; }
td.title2 { background:#D9E2F3; width:78%; }
td.title2 .en { font-size:15pt; font-weight:bold; color:#1F3864; display:block; }
.spacer { height:2pt; }
.intro { font-family:"Carlito","Calibri",sans-serif; font-size:9.5pt; font-style:italic; margin:0 0 8pt 0; }
.dlg { font-family:"Carlito","Calibri",sans-serif; font-size:11pt; line-height:1.3; margin:0 0 8pt 0; }
"""


def esc(t):
    return html.escape(t)


def render_and_count(lesson):
    lid = lesson['lesson_id']
    parts = [
        '<div class="title">EVERYDAY ENGLISH REFLEX</div>',
        '<div class="subtitle">&nbsp;</div>',
        '<table class="hdr"><tr>',
        f'<td class="cefr"><div class="lvl">{esc(lesson.get("cefr", "A0 / Pre-A1"))}</div><div class="lid">LESSON {esc(lid)}</div></td>',
        f'<td class="title2"><span class="en">{esc(lesson.get("en_title", "Lesson " + lid))}</span></td>',
        '</tr></table><div class="spacer"></div>',
        f'<div class="intro">{esc(lesson.get("intro_en", ""))}</div>',
    ]
    for speaker, en, vi in lesson['turns']:
        parts.append(f'<div class="dlg"><b>{esc(speaker)}:</b> {esc(en)}</div>')
    body = ''.join(parts)
    doc = f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{PAGE_CSS}</style></head><body>{body}</body></html>'
    os.makedirs(TMP_DIR, exist_ok=True)
    html_path = os.path.join(TMP_DIR, f'lesson{lid}.html')
    pdf_path = os.path.join(TMP_DIR, f'lesson{lid}.pdf')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(doc)
    subprocess.run(
        [CHROME, "--headless", "--no-sandbox", "--disable-gpu",
         f"--print-to-pdf={pdf_path}", "--print-to-pdf-no-header",
         "--no-pdf-header-footer", f"file://{html_path}"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30,
    )
    data = open(pdf_path, 'rb').read()
    return len(re.findall(rb'/Type\s*/Page(?!s)', data))


def main():
    lid = sys.argv[1].zfill(4)
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, here)
    if lid == '0001':
        from build_combined import load_lesson0001_as_dict
        lesson = load_lesson0001_as_dict(os.path.join(here, "lesson0001_approved.docx"))
        lesson['cefr'] = 'A0 / Pre-A1'
        lesson['en_title'] = 'Lesson 0001'
    else:
        mod = importlib.import_module(f"lesson{lid}")
        lesson = getattr(mod, f"LESSON_{lid}")
    pages = render_and_count(lesson)
    status = "PASS" if pages >= 5 else "FAIL"
    print(f"Lesson {lid}: {pages} real English-only A4 pages (target >= 5) -> {status}")


if __name__ == "__main__":
    main()
