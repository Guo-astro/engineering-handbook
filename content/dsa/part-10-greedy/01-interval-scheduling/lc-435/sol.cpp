// LC 435. Non-overlapping Intervals
//
// Sort by END ascending; walk; drop on overlap, otherwise advance the cursor.
// std::sort with a strict weak ordering on int avoids the subtraction-
// overflow bug; we never compute a[1] - b[1].
#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        std::sort(intervals.begin(), intervals.end(),
                  [](const std::vector<int>& a, const std::vector<int>& b) {
                      return a[1] < b[1];  // sort by END
                  });
        int removed = 0;
        int currentEnd = INT_MIN;
        for (const auto& iv : intervals) {
            if (iv[0] < currentEnd) {
                // Overlap: drop this interval; keep the earlier-ending one.
                ++removed;
            } else {
                currentEnd = iv[1];
            }
        }
        return removed;
    }
};
