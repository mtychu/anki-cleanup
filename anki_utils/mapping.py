"""Mapping utilities: load/save mapping files and suggest mappings.

This module is intentionally lightweight and depends on either PyYAML (preferred)
or the standard library `json` as a fallback so the repository remains usable
without extra dependencies for now.
"""

from typing import Dict, List
import os
import json

try:
    import yaml

    _HAS_YAML = True
except Exception:
    yaml = None
    _HAS_YAML = False

from difflib import get_close_matches


def load_mapping(path: str) -> Dict:
    """Load a mapping file from YAML or JSON.

    Returns an empty dict if the file doesn't exist or can't be parsed.
    """
    if not os.path.exists(path):
        return {}

    with open(path, "r", encoding="utf8") as fh:
        text = fh.read()

    if _HAS_YAML:
        try:
            return yaml.safe_load(text) or {}
        except Exception:
            # fallback to json
            pass

    try:
        return json.loads(text)
    except Exception:
        return {}


def save_mapping(path: str, mapping: Dict) -> None:
    """Save a mapping dict to disk using YAML when available, otherwise JSON."""
    dirname = os.path.dirname(path)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)

    if _HAS_YAML:
        with open(path, "w", encoding="utf8") as fh:
            yaml.safe_dump(mapping, fh, sort_keys=False, allow_unicode=True)
        return

    with open(path, "w", encoding="utf8") as fh:
        json.dump(mapping, fh, indent=2, ensure_ascii=False)


def suggest_mapping(
    model_fields: List[str], canonical_fields: List[str]
) -> Dict[str, str]:
    """Return a suggested mapping from model_fields -> canonical_fields.

    Uses simple difflib-based closeness matching. Caller should still confirm
    suggestions before applying them in bulk.
    """
    mapping: Dict[str, str] = {}
    canonical_low = {f.lower(): f for f in canonical_fields}

    for mf in model_fields:
        candidates = get_close_matches(mf, canonical_low.keys(), n=1, cutoff=0.6)
        if candidates:
            mapping[mf] = canonical_low[candidates[0]]
        else:
            # fallback to identity (user will likely override)
            mapping[mf] = mf

    return mapping
