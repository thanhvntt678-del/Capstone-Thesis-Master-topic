# MASTER V3 — FINAL UPDATE COMMAND (supersedes PROJECT_RULES.md where conflicting)

Source: `CLAUDE_BOOK_MASTER_ZERO_TO_B2_2000_SITUATIONS_FINAL_V3.xlsx` + the
"FINAL UPDATE COMMAND" chat message that accompanied it. This is now the
governing spec for the book. Where it conflicts with `PROJECT_RULES.md`
(the earlier "Lesson 001–401" spec), **this file wins**.

## Scope right now: BOOK ONLY
Read → audit → write/rewrite → edit → format → render book → count → QC →
self-correct → export book file. **No Excel conversion, Python data export,
TTS, subtitle, or MP4 production at this stage** — that comes later, as a
separate phase.

## Numbering: Situation 0001 → 2000 (not "Lesson")
- 001–400: Foundation → A1
- 401–800: A2
- 801–1200: B1
- 1201–1600: B1+
- 1601–2000: B2
- 2000 is a planning target, not a ceiling — continue 2001+ if final B2
  mastery audit finds essential gaps. Never pad to hit a number.

## DGE0001–0401 = source content, must be rewritten in
Preserve useful real-life situation, communicative purpose, and learning
value. Fix: unnatural English, spelling/grammar/syntax errors, unnatural
collocation, wrong register, mechanical dialogue, unrealistic conversation,
repetition, duplicate sentences, literal Vietnamese, unnatural Vietnamese,
wrong pronouns, weak situation, wrong CEFR, generic Person A/B, unnecessary
contractions, poor formatting. Situation 402+ is newly written.

## Characters — hard rule
**Ms Lan** is the fixed main character throughout the entire book. Every
Situation has **exactly Ms Lan + ONE other named, context-appropriate
character** (e.g. Mr David, Ms Emma, Mr James). `Person A` / `Person B` /
`Speaker A/B` / unnamed speakers are **forbidden**. Exactly 2 active
speakers per Situation (third parties may be mentioned by name, never given
a speaking turn).

## English: full-form only
Do not proactively use contractions (I'm, you're, it's, don't, can't,
won't, isn't, let's, etc. — expand all of them). Full-form English must
still read as natural, contemporary, natural-collocation, CEFR-appropriate
communication — never stiff or Google-Translate-shaped just because it's
full-form.

## Vietnamese: situational, never word-for-word
Meaning → real-life situation → communicative intention → tone →
politeness → relationship → natural Vietnamese. Word order/structure may
change freely from the English. Word-for-word translation, English-shaped
Vietnamese, meaning loss/addition, wrong tone, wrong pronoun = all hard 0.

## Layout — inline, no labels, no images
One format example only (layout reference, never repeat as content):
`Ms Lan: Excuse me, is anyone sitting here?  Xin lỗi, chỗ này có người ngồi chưa ạ?`
Character name (bold) + English + Vietnamese stay on the **same visual
row** whenever width permits — natural word-wrap only, never a forced line
break, never `English:` / `Tiếng Việt:` / `Vietnamese:` labels. Long turns
wrap naturally within the same turn — never split into fake turns.
**Zero images**, zero placeholders, zero blank image zones. No Vocabulary
list, no standalone Grammar lecture. SCM sample is visual reference only
(navy/deep-blue hierarchy, pale-blue section bars, typography, spacing,
margins, header/footer, page numbers) — never its content structure.

## Word/page accounting
- Typical Situation: ~300–340 English *learning* words when natural (not a
  quota — never pad; never under-write a genuinely bigger situation).
- Count English dialogue content only — never Vietnamese, names, titles,
  headings, footer, page numbers, design text.
- English-only A4 equivalent = English words / 500 (a content-equivalent
  metric only).
- **Actual bilingual rendered page count must be reported separately from
  actual rendered output — never estimated from the word count.** (Note:
  in this sandbox, LibreOffice's `--convert-to pdf` fails to load any
  source file, confirmed on a blank test document — an environment
  limitation, not a document defect. Actual page counts are reported as a
  manual layout estimate — average characters/line at the specified font,
  margins, and line-height, converted to line count → content height →
  pages — and explicitly flagged as an estimate, not a verified render,
  until a working renderer is available.)
- Whole-book planning range: 650,000–800,000 English words ≈ 1,300–1,600
  English-only A4-equivalent pages. Planning range, not a quota.

## Duplication / blank-page hard fails
Exact duplicate English sentences = 0. Artificial near-duplicate/template
padding = 0 (no same-skeleton-different-name filler). Blank pages = 0,
accidental near-blank pages = 0, no page-count manipulation (font/margin/
spacing tricks, hidden text, clipping, truncation).

## Topic mastery (Rule set, applied only where relevant to the topic)
Understand, respond, ask, follow up, clarify, confirm, explain, request,
accept, refuse, give reasons, change a request/decision, offer an
alternative, compare options, handle a problem/delay/mistake/refusal/
misunderstanding, respond to unexpected input, paraphrase, repair,
negotiate, compromise, solve the problem, confirm the result, close
naturally. A Major Topic may take as many Situations as it genuinely needs
(no fixed count per topic) and only advances to a new topic when
`TOPIC_MASTERY = PASS`; otherwise `CONTINUE SAME TOPIC`.

## Workflow — ONE Situation at a time, then STOP
`READ → AUDIT → WRITE/REWRITE → FORMAT → RENDER → COUNT ENGLISH WORDS →
CALCULATE ENGLISH A4 EQUIVALENT → COUNT ACTUAL BILINGUAL PAGES → ENGLISH QC
→ VIETNAMESE QC → CHARACTER QC → DIALOGUE QC → CEFR QC → DUPLICATION QC →
PAGE QC → PUBLICATION QC → SELF-CORRECT ALL FAILURES → RENDER AGAIN → FINAL
QC → EXPORT BOOK FILE → REPORT → STOP.` A failed Situation is never
delivered — fix, re-render, re-count, re-QC until FINAL QC = PASS.

**NEXT LOCK (absolute, overrides every earlier "keep writing" instruction):**
after one Situation is delivered with FINAL QC = PASS and its QC report
sent, **stop completely**. Do not draft, prepare, or start the next
Situation. Only resume when the user sends `NEXT`.

## Whole-book completion gate
Reaching Situation 2000 alone proves nothing. The book is only complete
when life-domain coverage, Foundation→B2 progression, core situations,
common problems, unexpected variations, follow-up, clarification,
paraphrase, repair, negotiation/compromise (where relevant), independent
problem solving, transfer to unfamiliar situations, English QC, Vietnamese
QC, duplication QC, and publication QC all PASS. Any essential gap →
continue 2001+, never pad.

## Where this project currently stands relative to the old system
The earlier `data/lessons/lesson_001.json`–`lesson_020.json` (Modules 1–2,
Person A/Person B format, contractions allowed) predate this Master V3 and
do not comply with it (wrong character system, contractions, wrong
numbering, wrong layout). They are **superseded, not deleted**. The active
system going forward is `book/situations/situation_NNNN.json` →
`scripts/build_book_docx.py` → `book/manuscript/PRACTICAL_EVERYDAY_ENGLISH_BOOK.docx`.
Situation 0001 = DGE0001 (same source mapping the old Lesson 001 used, now
rewritten under the Ms Lan / Mr David system). Situations 0002–0020 will
revisit the same DGE source situations the old Lessons 002–020 covered,
rewritten under the new rules, one at a time, only on explicit `NEXT`.
