# LC 189. Rotate Array
# Three-reverse trick: reverse the whole array, then reverse the first k,
# then reverse the rest. Avoids the O(n*k) naive shift. O(n), O(1).
from typing import List


def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    if n == 0:
        return
    k %= n  # Tolerate k > n; rotating n is a no-op.

    def _reverse(lo: int, hi: int) -> None:
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    _reverse(0, n - 1)
    _reverse(0, k - 1)
    _reverse(k, n - 1)
