# QuickNote

QuickNote is a simple command‑line tool to add and list notes stored in a local text file.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/quicknote.git
cd quicknote

# (Optional) Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate
```

> The script uses only the Python standard library, so no additional packages are required.

## Usage

```bash
# Add a note
python quicknote.py add "Buy milk"

# List all notes
python quicknote.py list
```

## Commands

- `add "note"` – Append a note with a timestamp.
- `list` – Display all notes in chronological order.

## Where are notes stored?

Notes are saved in a hidden file named `.quicknote.db` located in your home directory (`~/.quicknote.db`).
