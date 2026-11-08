"""L-099: total video includes the end card; estimates never certify actual media."""
import math

TARGET_SECONDS = (120.0, 180.0)
HARD_LIMIT_SECONDS = 300.0
# Descriptive fallback only, not a required delivery rate or word budget.
NATURAL_WORDS_PER_SECOND = 2.9


def duration_status(total):
    """Return error/warning/ok. No rounding before the strict upper-bound test."""
    total = float(total)
    if not math.isfinite(total) or total < 0 or total >= HARD_LIMIT_SECONDS:
        return "error"
    return "ok" if TARGET_SECONDS[0] <= total <= TARGET_SECONDS[1] else "warning"


def estimated_total(spoken_words, endcard_seconds=0, pause_seconds=0, transition_seconds=0):
    """ƯỚC at natural reading pace, plus end card; replace with a human estimate if available."""
    return (spoken_words / NATURAL_WORDS_PER_SECOND + float(endcard_seconds)
            + float(pause_seconds) + float(transition_seconds))
