"""Scheduler helpers for copying or transforming learning/scheduling data.

Scheduling data (intervals, ease, reps, due dates) is sensitive. This module
should contain functions that encapsulate the safe policies for transferring
progress from one card to another (for example, take the higher of the two
intervals, or preserve review counts but not the due date).

Start here for any code that touches Anki's scheduling fields.
"""

from typing import Dict


def safe_merge_schedule(
    old_card: Dict, new_card: Dict, policy: str = "conservative"
) -> Dict:
    """Return a scheduling dict to apply to `new_card` based on `old_card`.

    This is a placeholder; concrete policies should be implemented and
    thoroughly tested against a backup of the Anki collection.
    """
    # Example policy: conservative -> keep the card with higher interval/rep
    return {}
