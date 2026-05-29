// LC 912. Sort an Array
// Quicksort with median-of-three Lomuto partition.
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> sortArray(std::vector<int>& nums) {
        std::vector<int> arr = nums;
        if (arr.size() > 1) {
            quicksort(arr, 0, static_cast<int>(arr.size()) - 1);
        }
        return arr;
    }

private:
    static void quicksort(std::vector<int>& arr, int lo, int hi) {
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] < arr[lo]) std::swap(arr[lo],  arr[mid]);
            if (arr[hi]  < arr[lo]) std::swap(arr[lo],  arr[hi]);
            if (arr[mid] < arr[hi]) std::swap(arr[mid], arr[hi]);
            int p = lomutoPartition(arr, lo, hi);
            if (p - lo < hi - p) {
                quicksort(arr, lo, p - 1);
                lo = p + 1;
            } else {
                quicksort(arr, p + 1, hi);
                hi = p - 1;
            }
        }
    }

    static int lomutoPartition(std::vector<int>& arr, int lo, int hi) {
        int pivot = arr[hi];
        int i = lo - 1;
        for (int j = lo; j < hi; ++j) {
            if (arr[j] <= pivot) {
                ++i;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[hi]);
        return i + 1;
    }
};
