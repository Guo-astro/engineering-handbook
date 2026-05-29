# LC 3. Longest Substring Without Repeating Characters
from collections import Counter


def length_of_longest_substring(s: str) -> int:
    """LC 3 (last-index-jump form).

    For each new character, if it has been seen at index `prev` AND that
    `prev` lies inside the current window (`prev >= l`), jump l to prev + 1
    in O(1). Otherwise advance only r. The `last[ch] >= l` guard is what
    keeps stale entries from outside the window from causing a wrong jump.
    """
    last: dict[str, int] = {}
    l = 0
    best = 0
    for r, ch in enumerate(s):
        if ch in last and last[ch] >= l:
            l = last[ch] + 1
        last[ch] = r
        if r - l + 1 > best:
            best = r - l + 1
    return best


def length_of_longest_substring_shrink(s: str) -> int:
    """LC 3 (explicit shrink-loop form).

    The "obvious extension" of the fixed-window template: keep a frequency
    counter; when the new character's count exceeds 1, shrink l one step
    at a time until the duplicate is gone. Same O(n) amortized bound as
    the last-index-jump form, but with worse per-step worst case.
    """
    counts: Counter[str] = Counter()
    l = 0
    best = 0
    for r, ch in enumerate(s):
        counts[ch] += 1
        while counts[ch] > 1:
            counts[s[l]] -= 1
            l += 1
        if r - l + 1 > best:
            best = r - l + 1
    return best
