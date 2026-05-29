# LC 5. Longest Palindromic Substring
from typing import Tuple


def longest_palindrome(s: str) -> str:
    """LC 5: longest contiguous palindromic substring of s.

    Expand around each of the 2n - 1 candidate centers (n character-centers
    plus n - 1 between-character centers). For each center, push outward
    while s[left] == s[right]; the loop terminates one step past the last
    valid match, so the maximal palindrome is s[left+1 : right] when the
    helper returns the corrected (left+1, right-1) pair.
    O(n^2) time, O(1) extra space.
    """
    if not s:
        return ""

    def expand(left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    best_l, best_r = 0, 0
    for i in range(len(s)):
        l1, r1 = expand(i, i)            # odd-length center at i
        l2, r2 = expand(i, i + 1)        # even-length center between i and i+1
        if r1 - l1 > best_r - best_l:
            best_l, best_r = l1, r1
        if r2 - l2 > best_r - best_l:
            best_l, best_r = l2, r2
    return s[best_l:best_r + 1]
