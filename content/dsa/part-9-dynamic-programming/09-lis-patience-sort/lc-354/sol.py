# LC 354. Russian Doll Envelopes
from bisect import bisect_left
from typing import List


def length_of_lis(nums: List[int]) -> int:
    """LC 300 helper. Length of the longest strictly increasing subsequence."""
    tails: List[int] = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def max_envelopes(envelopes: List[List[int]]) -> int:
    """LC 354. Sort by (width ASC, height DESC on tie), then LIS on heights."""
    if not envelopes:
        return 0
    envelopes.sort(key=lambda e: (e[0], -e[1]))
    return length_of_lis([e[1] for e in envelopes])
