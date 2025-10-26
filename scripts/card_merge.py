from anki_utils.anki_connect import invoke

# Run using '-m' flag (i.e. python -m scripts.card_merge)


# Print data for a specific card
def card_info(card_id, deck_name=None):
    try:
        card_id = int(card_id)
    except ValueError:
        raise ValueError("Card ID must be an integer.")

    card_info = invoke("cardsInfo", cards=[card_id])
