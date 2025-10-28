# Anki Cleanup Scripts

A collection of scripts to automate, clean up, and streamline Anki deck management.

---

## Features

### 🔊 OpenAI TTS & Example Sentences

Automatically fetch example sentences and audio files for a given word and language using OpenAI.

- Generates multiple example sentences
- If the generated sentences are understandable, they are added to the deck
- If not, the script regenerates until suitable examples are found
- Audio files are attached to cards for listening practice

---

### 🔄 Card Merge

When importing new decks, you often encounter cards for words you already know. This script scans new cards and transfers progress from existing cards, ensuring you don’t lose history or duplicate effort.

- Detects overlapping cards between old and new decks
- Preserves review history and learning progress
- Optionally merges metadata (tags, example sentences, audio)
- Prioritizes new cards when conflicts arise (since they often contain better context)

---

## Development Notes

### 📝 Standard Note Type (Prework)

To support both **Chinese** and **Japanese**, a unified note type should be defined.

1. **Field Mapping**

   - Identify fields common across note types
   - Use user input to map fields from one note type to the standard format
   - (Future idea: add a GUI for field mapping)

   **Pseudocode:**

   ```text
   get all note types
   get list of fields for each note type
   prompt user to map fields → standard format
   store mapping in dictionary (per deck)
   ```
