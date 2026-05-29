# LC 435. Non-overlapping Intervals
#
# Sort by END ascending. Walk left to right. Keep the first interval; for
# each subsequent interval, drop it if it overlaps the last kept end,
# otherwise keep it and update the cursor. Return the drop count.
#
# Why sort-by-end and not sort-by-start: see the chapter's exchange-argument
# section. Sort-by-start fails on inputs like [[1,100],[2,3],[3,4]] — it
# greedily keeps [1,100], drops both shorter intervals, returns 2; the
# optimum is to keep [2,3] and [3,4], drop [1,100], for a count of 1.
from typing import List
import math


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """LC 435: minimum number of intervals to remove so the rest are non-overlapping."""
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])  # sort by END
    removed = 0
    current_end = -math.inf
    for start, end in intervals:
        if start < current_end:
            # Overlap: drop this interval (keep the earlier-ending one we already chose).
            removed += 1
        else:
            # No overlap: extend the schedule by adopting this interval.
            current_end = end
    return removed
