// LC 88. Merge Sorted Array
// Merge nums2 (length n) into nums1 (capacity m+n, first m valid) in place.
// Walk back-to-front so writes never overwrite an unread value. O(m+n), O(1).
#include <vector>

void merge(std::vector<int>& nums1, int m,
           std::vector<int>& nums2, int n) {
    int i = m - 1, j = n - 1, k = m + n - 1;
    while (j >= 0) {
        // Short-circuit on i >= 0 handles the m == 0 case implicitly.
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
}
