# LC 187. Repeated DNA Sequences
from typing import List


def find_repeated_dna_sequences(s: str) -> List[str]:
    """LC 187: 10-letter substrings that repeat, encoded 2 bits per base."""
    if len(s) < 10:
        return []
    code = {"A": 0, "C": 1, "G": 2, "T": 3}
    mask = 0
    MASK20 = (1 << 20) - 1               # keep low 20 bits == 10 bases
    seen: dict = {}
    answer: List[str] = []
    for i, c in enumerate(s):
        mask = ((mask << 2) | code[c]) & MASK20
        if i >= 9:                       # full 10-letter window in mask
            seen[mask] = seen.get(mask, 0) + 1
            if seen[mask] == 2:
                answer.append(s[i - 9 : i + 1])
    return answer
