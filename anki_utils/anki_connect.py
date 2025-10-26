import requests


# Define Global Variables for Anki
ANKI_CONNECT_URL = "http://localhost:8765"


# wrapper to send request to AnkiConnect
def invoke(action, **params):
    try:
        response = requests.post(
            ANKI_CONNECT_URL,
            json={"action": action, "version": 6, "params": params},
            timeout=5,
        )
    except requests.exceptions.ConnectionError:
        print(
            "ERROR: Couldn't connect to Anki. Please ensure Anki is running with AnkiConnect installed."
        )
        return None
    except requests.exceptions.Timeout:
        print("ERROR: Request to AnkiConnect timed out.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"ERROR: HTTP error: {e}")
        return None
    except Exception as e:
        print(f"ERROR: unexepected error om request {e}")
        return None

    # If no errors from AnkiConnect, parse response
    try:
        result = response.json()
        # print(result)
    except ValueError:
        print("ERROR: couldn't parse response object from AnkiConnect.")
        return None

    if result.get("error"):
        print(f"ERROR: AnkiConnect error: {result['error']}")
        return None

    return result.get("result")


# Function to find all decks
def find_decks():
    decks = invoke("deckNames")
    return decks or []


# Function to find card IDs in a specific deck
def card_ids(deck_name):
    # Validate deck_name is in decks
    decks = find_decks()

    if deck_name not in decks:
        raise ValueError(f"Deck '{deck_name}' does not exist. Available decks: {decks}")

    return invoke("findCards", query=f'deck:"{deck_name}"')


# Function to get info for a specific card ID and Deck
def card_info(card_id, deck_name=None):
    # Validate card_id is an integer
    try:
        card_id = int(card_id)
    except ValueError:
        raise ValueError("Card ID must be an integer.")

    card_info = invoke("cardsInfo", cards=[card_id])
    if not card_info:
        return None

    card_info = card_info[0]  # Get the first (and only) card info

    # If deck_name is provided, validate the card exiists in that deck
    if deck_name and card_info.get("deckName") != deck_name:
        return None

    return card_info
