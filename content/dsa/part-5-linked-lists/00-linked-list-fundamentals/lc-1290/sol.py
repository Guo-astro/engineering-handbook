# LC 1290. Convert Binary Number in a Linked List to Integer
"""Single-pass walk with a running accumulator. Each node holds 0 or 1;
shift the result left and OR in the current bit.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        curr = head
        while curr is not None:
            result = (result << 1) | curr.val
            curr = curr.next
        return result
