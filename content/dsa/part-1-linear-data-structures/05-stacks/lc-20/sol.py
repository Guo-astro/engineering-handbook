# LC 20. Valid Parentheses
# Push openers; on a closer, peek the top opener and pop iff it matches.
# Keying the pair table by closer ('(' is the value, ')' is the key) keeps
# the lookup branch-free. The terminal stack-empty check rejects unmatched
# openers. O(n), O(n).
from typing import List


def is_valid(s: str) -> bool:
    pair = {")": "(", "]": "[", "}": "{"}
    stack: List[str] = []
    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if not stack or stack[-1] != pair[c]:
                return False
            stack.pop()
    return not stack
