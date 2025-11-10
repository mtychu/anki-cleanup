"""Core merge logic skeleton.

This module will eventually contain the logic to match cards between two decks
and produce (or apply) a set of updates that preserve progress and merge
content according to a policy. For now it provides a small `Merger` class
with clear extension points and docstrings.
"""

from typing import Dict, List, Optional

from .anki_connect import invoke
from .mapping import load_mapping


class Merger:
    """High-level Merger orchestrates matching and merging.

    Attributes:
        mapping: dict-like object describing how model fields map to canonical fields.
    """

    def __init__(self, mapping_path: Optional[str] = None):
        self.mapping = {}
        if mapping_path:
            self.mapping = load_mapping(mapping_path) or {}

    def find_matches(
        self, old_deck: str, new_deck: str, key_fields: List[str]
    ) -> List[Dict]:
        """Discover candidate matches between `old_deck` and `new_deck`.

        Returns a list of match dictionaries describing the candidate pairs and
        a confidence score. This is a placeholder that should be implemented
        using batched `cardsInfo` calls and an index on the lookup key(s).
        """
        raise NotImplementedError("match-finding not implemented yet")

    def apply_merge(self, matches: List[Dict], commit: bool = False) -> List[Dict]:
        """Apply the planned merges.

        If `commit` is False, this should return a dry-run plan describing what
        would be changed. If True, it should perform the AnkiConnect calls to
        update cards and return a list of applied changes.
        """
        raise NotImplementedError("apply_merge not implemented yet")
