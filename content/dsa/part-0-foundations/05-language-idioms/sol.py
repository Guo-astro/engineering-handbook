from collections import Counter


def count_freqs(s: str) -> dict[str, int]:
    """Return a frequency map of characters in s using Counter."""
    return dict(Counter(s))
