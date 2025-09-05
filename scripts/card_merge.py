from anki_utils.anki_connect import invoke

# Test
decks = invoke("deckNames")
if decks:
    print("Decks in Anki:")
    for deck in decks:
        print("-", deck)
