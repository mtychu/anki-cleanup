"""Small utility helpers used across the project.

Keep pure helpers here (no AnkiConnect calls) so they are easy to unit test.
"""

from typing import Iterable, List
import re


def chunked(iterable: Iterable, size: int) -> List[List]:
    """Yield successive chunks of `size` from `iterable`.

    Returns a list of lists for simplicity in this small project.
    """
    it = list(iterable)
    return [it[i : i + size] for i in range(0, len(it), size)]


def normalize_text(s: str) -> str:
    """Return a normalized string suitable for fuzzy matching.

    Lowercase, strip punctuation and excess whitespace.
    """
    if s is None:
        return ""
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^\w\s]", "", s)
    return s.strip()
