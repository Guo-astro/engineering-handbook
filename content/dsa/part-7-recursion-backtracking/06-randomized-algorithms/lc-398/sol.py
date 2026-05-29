# LC 398. Random Pick Index
import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        """Reservoir sampling, k = 1. One scan, O(1) extra space.

        After processing the i-th match (1-indexed), every match seen so
        far is the current pick with probability exactly 1/i. The trick:
        when the i-th match arrives, replace the current pick with
        probability 1/i (i.e., when randint(1, i) == 1).
        """
        chosen_idx = -1
        match_count = 0
        for idx, value in enumerate(self.nums):
            if value != target:
                continue
            match_count += 1
            # Replace with probability 1/match_count.
            if random.randint(1, match_count) == 1:
                chosen_idx = idx
        return chosen_idx
