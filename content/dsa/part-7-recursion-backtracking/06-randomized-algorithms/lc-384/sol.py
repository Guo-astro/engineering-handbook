# LC 384. Shuffle an Array
import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.original = list(nums)

    def reset(self) -> List[int]:
        return list(self.original)

    def shuffle(self) -> List[int]:
        arr = list(self.original)
        # Durstenfeld: i descends from n-1 down to 1; j drawn uniformly from
        # [0, i] inclusive; swap arr[i] with arr[j]. The inclusive upper bound
        # is what makes the distribution uniform: dropping i from the range
        # produces Sattolo's algorithm (single-cycle permutations only).
        for i in range(len(arr) - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
