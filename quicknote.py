#!/usr/bin/env python3
"""quicknote.py – a tiny CLI note‑taking utility.

Provides two sub‑commands:
  - add "note"   : store a note with a timestamp
  - list         : display all stored notes
"""
import argparse
import os
import sys
from datetime import datetime

NOTE_DB = os.path.join(os.path.expanduser("~"), ".quicknote.db")


def ensure_db_exists() -> None:
    """Create the DB file if it does not exist."""
    if not os.path.isfile(NOTE_DB):
        open(NOTE_DB, "a", encoding="utf-8").close()


def add_note(note: str) -> None:
    """Append *note* with a timestamp to the DB file."""
    timestamp = datetime.now().isoformat(timespec="seconds")
    with open(NOTE_DB, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\t{note}\n")
    print(f"Added note at {timestamp}")


def list_notes() -> None:
    """Print all notes stored in the DB file."""
    if not os.path.isfile(NOTE_DB):
        print("No notes found.")
        return
    with open(NOTE_DB, "r", encoding="utf-8") as f:
        lines = [line.rstrip() for line in f if line.strip()]
    if not lines:
        print("No notes found.")
        return
    for line in lines:
        try:
            ts, note = line.split("\t", 1)
            print(f"[{ts}] {note}")
        except ValueError:
            # Fallback for malformed lines
            print(line)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="quicknote", description="Simple CLI note‑taking tool.")
    sub = parser.add_subparsers(dest="command", required=True)

    add_parser = sub.add_parser("add", help="Add a new note")
    add_parser.add_argument("note", nargs=argparse.REMAINDER, help="The note text")

    sub.add_parser("list", help="List all notes")
    return parser


def main(argv: list[str] | None = None) -> None:
    ensure_db_exists()
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        note_text = " ".join(args.note).strip()
        if not note_text:
            print("Error: note text cannot be empty.", file=sys.stderr)
            sys.exit(1)
        add_note(note_text)
    elif args.command == "list":
        list_notes()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
