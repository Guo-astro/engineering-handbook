# LC 274. H-Index (Medium)
# LC 1122. Relative Sort Array (Easy)
# LC 164. Maximum Gap (Hard)
# LC 451. Sort Characters By Frequency (Medium)
from collections import Counter
from typing import List


def counting_sort(nums: List[int]) -> List[int]:
    """Stable counting sort over bounded integer keys.

    Time:  O(n + k) where k = max(nums) - min(nums) + 1.
    Space: O(n + k).
    Stability: equal keys keep their relative order. The back-to-front
    walk (with decrement-before-write) is what makes that hold; forward
    scatter would invert it.
    """
    if not nums:
        return []
    lo = min(nums)
    hi = max(nums)
    k = hi - lo + 1
    count = [0] * k
    for x in nums:
        count[x - lo] += 1
    # Prefix sum: count[i] becomes the index AFTER the last slot for key (lo + i).
    for i in range(1, k):
        count[i] += count[i - 1]
    out = [0] * len(nums)
    # Walk input back-to-front to preserve stability.
    for x in reversed(nums):
        count[x - lo] -= 1
        out[count[x - lo]] = x
    return out


def h_index(citations: List[int]) -> int:
    """LC 274 H-Index via counting sort with the cap-at-n trick.

    The answer is bounded by n by definition (you cannot have an h-index
    higher than the number of papers you have written), so any citation
    count above n is structurally equivalent to n. Capping collapses the
    universe from arbitrary integers to [0, n], so counting sort runs in
    O(n) time and space regardless of the raw input range.
    """
    n = len(citations)
    count = [0] * (n + 1)
    for c in citations:
        count[min(c, n)] += 1
    total = 0
    for h in range(n, -1, -1):
        total += count[h]
        if total >= h:
            return h
    return 0


def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
    """LC 1122 Relative Sort Array. Constraints fix value range to [0, 1000],
    so a 1001-bucket count array always works. Once the count table exists,
    the emission order is a free design parameter: arr2's order first, then
    the remaining keys in ascending order.
    """
    count = [0] * 1001
    for x in arr1:
        count[x] += 1
    out: List[int] = []
    for x in arr2:
        out.extend([x] * count[x])
        count[x] = 0
    for v in range(1001):
        if count[v]:
            out.extend([v] * count[v])
    return out


def maximum_gap(nums: List[int]) -> int:
    """LC 164 Maximum Gap via pigeonhole bucket sort.

    Pigeonhole forces at least one of (n - 1) equal-width buckets to be
    empty, so the maximum gap MUST cross a bucket boundary. Each bucket
    only needs (min, max); the full sorted contents are not needed.
    Linear in n.
    """
    if len(nums) < 2:
        return 0
    lo, hi = min(nums), max(nums)
    if lo == hi:
        return 0
    n = len(nums)
    width = max(1, (hi - lo + n - 2) // (n - 1))
    n_buckets = (hi - lo) // width + 1
    INF = float("inf")
    bmin = [INF] * n_buckets
    bmax = [-INF] * n_buckets
    for x in nums:
        i = (x - lo) // width
        bmin[i] = min(bmin[i], x)
        bmax[i] = max(bmax[i], x)
    best = 0
    prev_max = lo
    for i in range(n_buckets):
        if bmin[i] == INF:
            continue
        best = max(best, int(bmin[i]) - prev_max)
        prev_max = int(bmax[i])
    return best


def frequency_sort(s: str) -> str:
    """LC 451 Sort Characters By Frequency via bucket sort indexed by
    occurrence count. The frequency of any character in a length-n string
    is in [1, n], so n + 1 frequency buckets cover every case; iterating
    buckets from n down to 1 emits in descending-frequency order.
    """
    freq = Counter(s)
    n = len(s)
    buckets: List[List[str]] = [[] for _ in range(n + 1)]
    for ch, f in freq.items():
        buckets[f].append(ch)
    out: List[str] = []
    for f in range(n, 0, -1):
        for ch in buckets[f]:
            out.append(ch * f)
    return "".join(out)


if __name__ == "__main__":
    cases = [
        ([4, 2, 2, 8, 3, 3, 1], [1, 2, 2, 3, 3, 4, 8]),
        ([], []),
        ([5, 5, 5], [5, 5, 5]),
        ([0, 1, 0, 2, 1, 0], [0, 0, 0, 1, 1, 2]),
        ([-3, -1, -2, 0, -1], [-3, -2, -1, -1, 0]),
    ]
    for nums, expected in cases:
        assert counting_sort(nums) == expected, (nums, expected)
    assert h_index([3, 0, 6, 1, 5]) == 3
    assert maximum_gap([3, 6, 9, 1]) == 3
    print("PASS")
