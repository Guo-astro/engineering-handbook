# LC 560. Subarray Sum Equals K
from collections import defaultdict
from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    """LC 560. Count contiguous subarrays whose sum equals k.

    Invariant: at index i (inclusive), the number of subarrays ending at i
    whose sum is k equals counts[prefix - k], where prefix is the running
    sum through i. Sum that quantity over all i.
    """
    counts: defaultdict[int, int] = defaultdict(int)
    counts[0] = 1  # empty-prefix seed: lets a subarray starting at index 0 hit
    prefix = 0
    answer = 0
    for x in nums:
        prefix += x
        # Look up BEFORE inserting the current prefix; otherwise a k=0 input
        # would pair the current index with itself (an empty subarray).
        answer += counts[prefix - k]
        counts[prefix] += 1
    return answer
