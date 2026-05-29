# LC 17. Letter Combinations of a Phone Number
from typing import List


KEYPAD = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combinations(digits: str) -> List[str]:
    """LC 17. Backtracking: each digit is one slot in the recursion tree."""
    if not digits:
        return []
    result: List[str] = []
    path: List[str] = []

    def backtrack(i: int) -> None:
        if i == len(digits):
            result.append("".join(path))
            return
        for letter in KEYPAD[digits[i]]:
            path.append(letter)        # 1. CHOOSE
            backtrack(i + 1)           # 2. EXPLORE
            path.pop()                 # 3. UNCHOOSE

    backtrack(0)
    return result
