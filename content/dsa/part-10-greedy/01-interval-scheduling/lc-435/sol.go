// LC 435. Non-overlapping Intervals
//
// Sort by END ascending; walk; drop on overlap, otherwise advance the cursor.
// math.MinInt32 sentinel works for LC 435's stated bound -5*10^4 <= start,
// end <= 5*10^4.
package main

import (
	"math"
	"sort"
)

func eraseOverlapIntervals(intervals [][]int) int {
	if len(intervals) == 0 {
		return 0
	}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1] // sort by END
	})
	removed := 0
	currentEnd := math.MinInt32
	for _, iv := range intervals {
		if iv[0] < currentEnd {
			// Overlap: drop this interval; keep the earlier-ending one.
			removed++
		} else {
			currentEnd = iv[1]
		}
	}
	return removed
}
