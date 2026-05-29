# LC 344. Reverse String
# Two-pointer in-place swap on a mutable character buffer.
# Python str is immutable, so the LC signature uses List[str]. O(n), O(1).
from typing import List


def reverse_string(s: List[str]) -> None:
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
