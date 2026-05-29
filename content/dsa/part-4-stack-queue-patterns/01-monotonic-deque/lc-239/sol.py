# LC 239. Sliding Window Maximum
from collections import deque
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """Return the maximum of every contiguous window of size k.

    Invariant: dq stores indices in strictly decreasing order of nums[index].
    The front index is therefore always the argmax of the current window.
    Indices, not values, so the head's age is checkable against i - k.
    """
    dq: deque[int] = deque()
    out: List[int] = []
    for i, x in enumerate(nums):
        # Drop indices that fell out of the left edge of the window.
        if dq and dq[0] <= i - k:
            dq.popleft()
        # Maintain decreasing monotonicity: any tail value <= x is dominated.
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
