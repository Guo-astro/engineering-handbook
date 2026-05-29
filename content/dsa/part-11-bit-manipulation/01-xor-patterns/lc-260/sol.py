# LC 260. Single Number III
#
# Phase 1: XOR all -> xor_all = a ^ b (the two unique values).
# Phase 2: isolate any bit where a and b differ (lowbit = xor_all & -xor_all),
# bucket by that bit, XOR each bucket. Each bucket is now an LC-136 instance.
from typing import List


def single_number(nums: List[int]) -> List[int]:
    """LC 260 — two elements appear once; all others appear twice."""
    xor_all = 0
    for x in nums:
        xor_all ^= x
    diff_bit = xor_all & -xor_all  # isolate the lowest bit where a and b differ
    a = b = 0
    for x in nums:
        if x & diff_bit:
            a ^= x
        else:
            b ^= x
    return [a, b]
