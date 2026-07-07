"""
store-hours-checker-skill: Client SDK
Evaluates operating time boundaries to update shop checkouts dynamically.
"""
from __future__ import annotations
from typing import Optional


class StoreHoursCheckerClient:
    """
    SDK for schedule verification.
    """

    def verify_status(
        self,
        current_hour: int,
        open_hour: int = 9,
        close_hour: int = 21,
    ) -> dict:
        # Wrap hours around 24
        ch = current_hour % 24
        oh = open_hour % 24
        chour = close_hour % 24

        # Standard daylight hour operation logic
        if oh < chour:
            is_open = oh <= ch < chour
        else:
            # Over-midnight operations window (e.g. 18:00 to 02:00)
            is_open = ch >= oh or ch < chour

        if is_open:
            next_change = (chour - ch) % 24
        else:
            next_change = (oh - ch) % 24

        return {
            "is_open": is_open,
            "next_change_hours": next_change,
            "current_status": "open" if is_open else "closed"
        }
