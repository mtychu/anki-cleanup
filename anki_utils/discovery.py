"""Discovery helpers for Anki models, fields and decks.

This module contains small convenience wrappers around the AnkiConnect
`invoke` function to discover available note types (models), model fields,
deck names and card ids. Keep these thin so they are easy to test and mock.
"""

from typing import List

from .anki_connect import invoke


def list_models() -> List[str]:
    """Return a list of model (note type) names.

    Returns an empty list when AnkiConnect is unavailable or the call fails.
    """
    return invoke("modelNames") or []


def model_fields(model_name: str) -> List[str]:
    """Return the field names for a model.

    If the model does not exist or the request fails, an empty list is returned.
    """
    return invoke("modelFieldNames", modelName=model_name) or []


def deck_names() -> List[str]:
    """Return a list of deck names.

    Normalizes AnkiConnect's return to an empty list on error.
    """
    return invoke("deckNames") or []


def card_ids(deck_name: str) -> List[int]:
    """Return a list of card IDs found in the given deck (by name).

    Uses Anki's search query via AnkiConnect. Returns an empty list on error.
    """
    return invoke("findCards", query=f'deck:"{deck_name}"') or []
