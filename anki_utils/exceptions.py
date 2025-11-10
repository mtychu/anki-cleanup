"""Domain-specific exceptions for the anki_utils package."""


class AnkiUnavailable(Exception):
    """Raised when AnkiConnect is unreachable or returns an error."""


class AmbiguousMatch(Exception):
    """Raised when multiple candidate matches exist and user confirmation is required."""
