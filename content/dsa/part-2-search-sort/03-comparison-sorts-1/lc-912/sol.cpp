// LC 912. Sort an Array (canonical merge sort, top-down with shared aux buffer)
#include <vector>

class Solution {
public:
    std::vector<int> sortArray(std::vector<int>& nums) {
        if (nums.size() <= 1) return nums;
        std::vector<int> arr = nums;
        std::vector<int> aux(arr.size());      // shared scratch buffer
        mergeSort(arr, aux, 0, (int)arr.size() - 1);
        return arr;
    }

private:
    void mergeSort(std::vector<int>& arr, std::vector<int>& aux, int lo, int hi) {
        if (lo >= hi) return;
        int mid = lo + (hi - lo) / 2;          // Bloch 2006 overflow-safe midpoint
        mergeSort(arr, aux, lo, mid);
        mergeSort(arr, aux, mid + 1, hi);
        if (arr[mid] <= arr[mid + 1]) return;  // Sedgewick algs4 §2.2.2 short-circuit
        merge(arr, aux, lo, mid, hi);
    }
    void merge(std::vector<int>& arr, std::vector<int>& aux, int lo, int mid, int hi) {
        for (int k = lo; k <= hi; ++k) aux[k] = arr[k];
        int i = lo, j = mid + 1;
        for (int k = lo; k <= hi; ++k) {
            if (i > mid)               arr[k] = aux[j++];
            else if (j > hi)           arr[k] = aux[i++];
            else if (aux[i] <= aux[j]) arr[k] = aux[i++];   // `<=` keeps stability
            else                       arr[k] = aux[j++];
        }
    }
};
