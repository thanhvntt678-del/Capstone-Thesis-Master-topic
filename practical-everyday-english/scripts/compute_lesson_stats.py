#!/usr/bin/env python3
"""QC stats for one RESTART Lesson JSON (Master 2000-Lesson system).

Counts English learning-dialogue words only (never Vietnamese, names,
titles, headings, footer, page numbers, design text) and checks for
banned contractions / exact duplicate lines / speaker count.
"""
import json
import re
import sys
from pathlib import Path

BANNED_CONTRACTIONS = [
    "I'm", "you're", "we're", "they're", "it's", "that's", "I've", "we've",
    "I'll", "I'd", "can't", "couldn't", "don't", "doesn't", "didn't",
    "won't", "wouldn't", "isn't", "aren't", "let's", "he's", "she's",
    "there's", "who's", "what's", "shouldn't", "haven't", "hasn't", "hadn't",
]


def word_count(text):
    if not text:
        return 0
    return len(re.findall(r"[A-Za-z']+", text))


def main(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    turns = data.get("turns", [])

    dialogue_words = sum(word_count(t["english"]) for t in turns)
    speakers = set(t["speaker"] for t in turns)

    contraction_hits = []
    for t in turns:
        for b in BANNED_CONTRACTIONS:
            if re.search(re.escape(b), t["english"], re.IGNORECASE):
                contraction_hits.append((t["turn_order"], b))

    seen = {}
    dups = []
    for t in turns:
        key = t["english"].strip().lower()
        if key in seen:
            dups.append((seen[key], t["turn_order"]))
        else:
            seen[key] = t["turn_order"]

    print(f"Lesson: {data['lesson_id']} — {data['english_title']}")
    print(f"CEFR: {data['cefr_level']}   Target words: {data['en_word_target']}   Target pages: {data['page_target']}")
    print(f"Dialogue turns: {len(turns)}")
    print(f"English dialogue words: {dialogue_words}")
    print(f"Distinct speakers: {speakers} (count={len(speakers)})")
    print(f"Banned contractions found: {contraction_hits if contraction_hits else 0}")
    print(f"Exact duplicate English lines: {dups if dups else 0}")


if __name__ == "__main__":
    main(sys.argv[1])
