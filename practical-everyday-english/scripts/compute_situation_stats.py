#!/usr/bin/env python3
"""Compute exact ENGLISH LEARNING WORD count for one Situation JSON file.

Per Master V3: count only English dialogue/content. Do not count
Vietnamese, speaker names, titles, headings, page numbers, footer or
design text.
"""
import json
import re
import sys
from pathlib import Path


def word_count(text):
    if not text:
        return 0
    return len(re.findall(r"[A-Za-z']+", text))


def check_contractions(text):
    banned = ["I'm", "you're", "we're", "they're", "it's", "that's", "I've", "we've",
              "I'll", "I'd", "can't", "couldn't", "don't", "doesn't", "didn't",
              "won't", "wouldn't", "isn't", "aren't", "let's", "he's", "she's",
              "there's", "who's", "what's", "shouldn't", "haven't", "hasn't", "hadn't"]
    found = []
    for turn in DATA.get("turns", []):
        eng = turn["english"]
        for b in banned:
            if re.search(re.escape(b), eng, re.IGNORECASE):
                found.append((turn["turn_order"], b))
    return found


def check_exact_duplicates():
    seen = {}
    dups = []
    for turn in DATA.get("turns", []):
        key = turn["english"].strip().lower()
        if key in seen:
            dups.append((seen[key], turn["turn_order"]))
        else:
            seen[key] = turn["turn_order"]
    return dups


def check_speakers():
    speakers = set(t["speaker"] for t in DATA.get("turns", []))
    return speakers


if __name__ == "__main__":
    path = Path(sys.argv[1])
    DATA = json.loads(path.read_text(encoding="utf-8"))

    total_words = word_count(DATA.get("context_note_en", ""))
    turn_words = 0
    for turn in DATA.get("turns", []):
        turn_words += word_count(turn["english"])
    total_dialogue_words = turn_words

    print(f"Situation: {DATA['situation_id']} — {DATA['english_title']}")
    print(f"Dialogue turns: {len(DATA.get('turns', []))}")
    print(f"English dialogue words (learning content): {total_dialogue_words}")
    print(f"Context note EN words (not counted in dialogue total): {word_count(DATA.get('context_note_en', ''))}")
    print(f"English-only A4 equivalent: {round(total_dialogue_words / 500, 3)}")
    print()
    speakers = check_speakers()
    print(f"Distinct speakers: {speakers} (count={len(speakers)})")
    contractions = check_contractions(DATA.get("context_note_en", ""))
    print(f"Banned contractions found: {contractions if contractions else 0}")
    dups = check_exact_duplicates()
    print(f"Exact duplicate English lines: {dups if dups else 0}")
