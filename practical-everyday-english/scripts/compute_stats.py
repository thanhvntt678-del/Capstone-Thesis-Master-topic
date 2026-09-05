#!/usr/bin/env python3
"""Compute TOTAL_ENGLISH_WORDS / ESTIMATED_ENGLISH_A4_PAGES across all lesson JSON files.

English word count = words in situation_title_en + context_note_en + every
turn's "english" field. Vietnamese text, IDs, and metadata are never counted
(Rule 15: English-only page tracking).
"""
import json
import sys
from pathlib import Path

LESSONS_DIR = Path(__file__).resolve().parent.parent / "data" / "lessons"
WORDS_PER_A4_PAGE = 500


def word_count(text):
    if not text:
        return 0
    return len(text.split())


def main():
    lesson_files = sorted(LESSONS_DIR.glob("lesson_*.json"))
    total_words = 0
    total_turns = 0
    per_lesson = []

    for path in lesson_files:
        data = json.loads(path.read_text(encoding="utf-8"))
        words = word_count(data.get("situation_title_en", ""))
        words += word_count(data.get("context_note_en", ""))
        for turn in data.get("turns", []):
            words += word_count(turn.get("english", ""))
            total_turns += 1
        total_words += words
        per_lesson.append((data["lesson_id"], data["situation_title_en"], words, len(data.get("turns", []))))

    est_pages = round(total_words / WORDS_PER_A4_PAGE, 2)

    print(f"Lessons found:        {len(lesson_files)}")
    print(f"Total dialogue turns: {total_turns}")
    print(f"TOTAL_ENGLISH_WORDS:  {total_words}")
    print(f"ESTIMATED_ENGLISH_A4_PAGES: {est_pages}")
    print()
    for lid, title, words, turns in per_lesson:
        print(f"  Lesson {lid}: {words:>4} EN words, {turns:>2} turns — {title}")

    return {
        "lessons_written": len(lesson_files),
        "total_turns": total_turns,
        "total_english_words": total_words,
        "estimated_english_a4_pages": est_pages,
    }


if __name__ == "__main__":
    main()
