# LC 643. Maximum Average Subarray I
from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    """LC 643. Maximum average over all length-k subarrays.

    Track the running sum across the slide. Postpone the division by k
    until the end so the float division runs once on the maximum sum.
    """
    n = len(nums)
    window_sum = sum(nums[:k])
    best_sum = window_sum
    for r in range(k, n):
        window_sum += nums[r] - nums[r - k]
        if window_sum > best_sum:
            best_sum = window_sum
    return best_sum / k
