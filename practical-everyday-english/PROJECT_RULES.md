# PRACTICAL EVERYDAY ENGLISH — MASTER PROJECT RULES

This file is the durable reference copy of the master rules supplied for this
project, so that any future work session can resume without needing the
rules re-pasted. It is the governing specification for everything under
`practical-everyday-english/`. Do not weaken, shorten, or reinterpret these
rules — follow them literally.

## 1. Goal
Write **PRACTICAL EVERYDAY ENGLISH — TIẾNG ANH GIAO TIẾP THỰC CHIẾN**, a book
taking learners from zero through A1 → A2 → B1 → B2 real-world communication.
Not a phrase-memorization book. Target competencies: UNDERSTAND → RESPOND →
FOLLOW UP → CLARIFY → EXPLAIN → REQUEST → REFUSE/ACCEPT → PARAPHRASE → REPAIR
MISUNDERSTANDING → ADAPT → NEGOTIATE → SOLVE PROBLEMS → CONFIRM → CLOSE
NATURALLY, including handling responses that differ from what was expected.

## 2. DGE001–401 source
Four source workbooks contain DGE0001–DGE0401 (topic/CEFR sequencing for the
first 401 situations). **The dialogue text in those workbooks is drill/TTS
pronunciation-practice script** (heavy phrase repetition, meta-instructional
lines like "say it slowly," no real communicative exchange) and fails the
naturalness/non-repetition/real-situation rules below. Per the master rule:
keep the good part (the topic, title, CEFR level, and sequencing — this *is*
kept, verified against `source_reference/DGE_video_index_001_401.csv`),
rewrite everything that is inadequate (nearly all of the dialogue text) into
complete, natural book content. Do not ask before fixing — self-QC and fix.
After 401, continue writing new lessons (402+) under the same standard.

## 3. No fixed video-count target
Curriculum is driven by **communicative mastery per topic**, not a video
quota. A major topic may need as many situations as it genuinely needs — no
mechanical fixed count per topic.

## 4. End a topic only on competence, not page count
Mark `TOPIC_MASTERY = PASS` only once the competencies relevant to that
topic are covered (as applicable — not every item applies to every topic):
understand, respond, ask follow-up, give information, request, explain,
clarify, confirm, choose, change a request, agree, refuse, offer an
alternative, repair misunderstanding, handle a problem, react to an
unexpected answer, paraphrase, self-correct, solve a problem, confirm an
outcome, close naturally.

## 5. Exactly two speakers
Every conversation is **Person A ↔ Person B** only. No four-person dialogues.
The Vietnamese translation is never a separate "speaker." Third parties may
be *mentioned* by name (e.g. "This is my colleague, Sam") but never take a
speaking turn. Speaker field is always literally `Person A` or `Person B`.

## 6. Mandatory dialogue table / data shape
Every conversation renders as: `No. | Speaker | English | Vietnamese
Translation`. English and Vietnamese are always separate fields, never
merged into one block. The machine-readable schema (matches Excel export):
`Lesson_ID, Major_Topic, Situation_ID, Situation_Title_EN, Situation_Title_VI,
CEFR, Turn_Order, Speaker, English, Vietnamese_Translation, Is_Learning_Text,
MP4_Part`. Python must never have to guess English vs Vietnamese, speaker,
or order.

## 7. English standard (locked)
Correct spelling, grammar, syntax, natural collocation, appropriate register
and politeness, correct CEFR, correct context, coherent dialogue, natural
spoken rhythm. **Natural Contemporary International English**, consistent
**British English** spelling/pronunciation standard. No stiff "textbook
English," no grammatically-correct-but-nobody-says-that sentences.

## 8. Real communicative reflex, not Q/A drilling
No mechanical Question1→Answer1, Question2→Answer2 pattern. Each turn reacts
to the one before. Where appropriate: opening → purpose → information
exchange → follow-up → clarification → choices/problems → reaction →
solution → confirmation → natural closing. Never force every situation into
one rigid template.

## 9. Natural reflexes by CEFR stage
Progressively introduce (per level): contractions, short reactions,
follow-up questions, clarification, checking understanding, self-correction,
paraphrasing, hesitation, polite interruption, softening, changing one's
mind, offering alternatives, partial agreement, polite disagreement,
repairing misunderstandings, natural closing. No slang stuffed in to fake
"native-ness."

## 10. Vietnamese translation standard
Translate meaning, context, intention, tone, politeness, emotion, and
relationship — never word-for-word. Never default I=tôi / you=bạn
mechanically; choose pronouns (tôi, mình, anh, chị, em, cô, chú, quý
khách...) based on the real relationship and register in each scene.

## 11. No vocabulary list, anywhere
No "Useful Vocabulary," "Vocabulary," "New Words," "Word List," or
Word=Meaning tables. All vocabulary must appear inside complete communicative
sentences. The visual/layout reference workbook (SCM sample) is for design
only (colours, banners, section bars, layout) — never copy its Vocabulary
section structure.

## 12. No standalone grammar lecture
No grammar-teaching block inserted into the learning text. Grammar is
absorbed through realistic dialogue and deliberate repetition across varied
situations.

## 13. Full life-domain coverage
Systematically cover essential life domains (self/identity, family, home,
neighbours, friends, relationships, emotions, food, restaurants, shopping,
returns/refunds, payments, banking, housing, utilities, repairs, health,
pharmacy, doctor, dentist, fitness, phone, internet, apps/tech, directions,
driving, taxi, bus, train, airport, flights, travel, hotels, holidays,
delivery, post, insurance, public services, official procedures, education,
community, events, emergencies, lost property, workplace, interviews,
colleagues, managers, customers, phone calls, meetings, presentations,
complaints, negotiation, conflict, opinions, decisions, plans, storytelling,
social interaction) — not limited to this list if another essential domain
is missing.

## 14. Real CEFR progression
- **A1**: basic needs, short clear sentences, simple reflexes.
- **A2**: handles everyday situations independently, more detail, choices,
  simple problems.
- **A2+**: flexible follow-up, clarification, situation changes.
- **B1**: explanation, reasons, experiences, storytelling, problem-handling.
- **B1+**: nuance, disagreement, boundaries, negotiation, paraphrase.
- **B2**: sustained interaction, unexpected input, nuanced opinions,
  persuasion, compromise, repair, paraphrasing, adaptation, independent
  problem-solving. B2 is not just longer sentences.

## 15. Page/word tracking — English only
Never count the Vietnamese translation, cover, table of contents, footer,
page numbers, images, or white space toward the page target. Track
`TOTAL_ENGLISH_WORDS` and `ESTIMATED_ENGLISH_A4_PAGES` (≈500 English
words/A4 page) separately. Planning range: **650,000–800,000 English
words**, ≈**1,300–1,600 A4 English-only pages**. This is a planning range,
not a quota — keep writing past it if B2 mastery isn't PASS yet; never pad
with meaningless repeated sentences once mastery already PASSed.

## 16. Professional book design from the start
Learn from the SCM sample only: navy/deep-blue hierarchy, pale-blue section
bars, CEFR badge, professional A4 layout, white space, clean tables,
contextual images, consistent footer, automatic page numbers. Never copy its
Vocabulary section. Each unit ideally has: series header, lesson/unit, CEFR,
English title, Vietnamese title, situation/context, realistic context image,
key situation info (only if truly needed), core dialogue, real-life
variation (if needed), integrated challenge (if fitting), footer, automatic
page number. Long content flows to a new page — never shrink font, cut
sentences, or cram content to fit one page.

## 17. Pre-publication QC gate
Before marking anything PASS: spelling, grammar, syntax, collocation,
naturalness, register, CEFR, conversation logic, Vietnamese translation,
topic focus, two-speaker rule, duplication, layout, overflow, pagination,
machine readability — all must PASS. Self-fix any FAIL; never hand the user
a failing draft.

## 18. Book is master for Python
Pipeline: BOOK → EXCEL → PYTHON → TTS → SUBTITLE → MP4. Never rewrite content
for video; never shorten into a "video script." Every English line and
Vietnamese line has its own field. Python must never guess English vs.
Vietnamese, speaker, or order.

## 19. Zero text loss
Never delete, shorten, summarise, truncate, omit, or ellipsis book content.
If audio would be long, extend the video; if subtitle text is long, wrap it;
if a topic is long, split MP4 into Part 1/2/3... at natural points without
cutting or rewriting the book content. The ~4-minute/video target is a later
packaging goal, never a content limit.

## 20. Run continuously
Start at Lesson 001, rewrite through 401, then continue 402, 403, ... without
asking "should I continue." On hitting a system limit, finish the current
unit, save `LAST_COMPLETE_LESSON`, `LAST_COMPLETE_SITUATION`,
`TOTAL_ENGLISH_WORDS`, `ESTIMATED_ENGLISH_A4_PAGES` to `PROGRESS.json`, and
resume from there next time — never redo PASSed work.

## 21. Whole-project completion gate
Only finish the entire project when ALL of: life-domain coverage, CEFR
zero→B2 coverage, core real-life situations, common problems, unexpected
variations, interaction strategies, paraphrase/repair, transfer to unfamiliar
situations, English QC, Vietnamese QC, publication QC, Python-ready data,
zero text loss, and final B2 mastery all PASS. If any essential item FAILs,
keep writing.

---

### Deviation from a literal rule, and why

- **Rule 2** required reading and rewriting DGE001–401 dialogue content. The
  actual dialogue text supplied is not usable communicative material (see
  above) — only the topic/CEFR sequencing survives into the book. This is
  exactly what Rule 2 itself instructs when source content fails QC
  ("nếu phát hiện ... English cứng ... dialogue rời rạc ... lặp câu/lặp cấu
  trúc ... thì TỰ SỬA. Không hỏi người dùng.") — so this is compliance with
  Rule 2, not a deviation from it.
