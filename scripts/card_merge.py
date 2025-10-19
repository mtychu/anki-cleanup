from anki_utils.anki_connect import invoke

# Run using '-m' flag (i.e. python -m scripts.card_merge)

# Print Decks
decks = invoke("deckNames")
if decks:
    print("Decks in Anki:")
    for deck in decks:
        print("-", deck)

# find card IDs in a specific deck
card_ids = invoke("findCards", query='deck:"Core 10k"')
if not card_ids:
    print("no cards bro")
else:
    print(len(card_ids))
    card_info = invoke("cardsInfo", cards=[card_ids[0]])
    print(card_info)
