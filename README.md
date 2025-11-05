# Anki Cleanup Scripts

A collection of scripts I'm using to clean up and automate my Anki Deck

## OpenAI TTS & Example Sentences

Given a word and language, automatically fetch example sentences and audio files from Open AI.

- if I can understand the sentences, then add them into the deck, otherwise regenerate.

## Card Merge

When adding new decks, you will often already have a lot of cards you already know. This script will scan the new cards, and transfer progress from words you already know to the new deck (or alternatively keep the old cards). This will retain all of your progress and history.

### TODO/Pseudocode

#### Prework

- develop standard note type to use going forwards. Should be applicable to both Chinese and Japanese

1. Check which fields are in common between note types

   - Use user input to map fields from one note type to a standard format
   - GUI? Maybe long-term

   pseudocode:

   - get all note types
   - get a list of fields for each note type
   - get user input to map fields to standard deck
   - maintain a dictionary for which fields belong to which in the standard format
     - one dictionary per deck to map to standard deck?

2. Loop through all cards in the deck we want to keep

   - For each card:

     - find corresponding card in the 'new' deck based on indicated field(s)
     - If word isn't in the new deck, do nothing
     - If word is found in the new deck, go to step 3

     pseudocode:

     - get full list of cards in old deck and new deck
       - loop through list of old cards
       - for each card, search in new cards (how do I do this not stupid?)
         - if word exists (based on indicated check field)
           - use mapping to bring new card into standard card format
           - use mapping to bring old card into standard card format
           - prioritize new card if conflicting since new context is better

3. Merge card information to existing card (and keep progress)

   - Update fields in 'old' deck card with data from 'old' deck card (e.g. add tags, update extra info)
     - Do I need to account for fields in the new card that don't exist in the old card?
     - Should I force a standard format? Yes?
   - If sentences are different then bring example sentence and audio over

## Add new Anki Card

A function that adds a card to the deck and moves it to the front of the learning queue. Intention is to allow people to continue to study a core 10K deck for example, but to move vocabulary that they're seeing in real life directly to reviews.

If a word that the user adds is already in the deck, info on that card should merge with whatever the user adds.

#### All Purpose Card - glyph

| Fields         | Sample Value Chinese   | Sample Value Japanese               | Notes                                      |
| -------------- | ---------------------- | ----------------------------------- | ------------------------------------------ |
| frequency      | 234                    | 387                                 |                                            |
| vocab          | 離職                   | 六つ                                |                                            |
| vocab_reading  | lízhí                  | むっつ                              |                                            |
| definition     | resign                 | six (things)                        |                                            |
| part_of_speech | verb                   | noun                                |                                            |
| vocab_ruby     | 離職[lízhí]            | 六[むっ]つ                          | ruby should work for chinese too           |
| example        | 我朋友都慢慢開始離職了 | "息子[むすこ]は  **六[むっ]つ**にな | anki can't hold arrays, need to split this |
| vocab_audio    | [sound:387V.opus]      | [sound:387V.opus]                   |                                            |
| example_audio  | [sound:387S.opus]      | [sound:387S.opus]                   |                                            |
| note_short     | synonyms?              | synonyms?                           | pitch accent, usage, etc                   |
| note_full      | AI/Human Note          | AI/Human Note                       |                                            |
| cloze_before   | 我朋友都慢慢開始       | 創真 まだまだ                       |                                            |
| cloze_inside   | 離職                   | 修業                                |                                            |
| cloze_after    | 了                     | が足りねぇな｡                       |                                            |
| context        | lesson                 | core10k                             | where did you get this card from?          |
| tags           |                        |                                     |                                            |
