# LC 88. Merge Sorted Array
# Merge nums2 (length n) into nums1 (capacity m+n, first m valid) in place.
# Walk back-to-front so writes never overwrite an unread value. O(m+n), O(1).
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        # Short-circuit on i >= 0 handles the m == 0 case implicitly.
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
