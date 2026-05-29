// LC 912. Sort an Array
// Quicksort with median-of-three Lomuto partition.
public class Sol {
    public int[] sortArray(int[] nums) {
        int[] arr = nums.clone();
        if (arr.length > 1) {
            quicksort(arr, 0, arr.length - 1);
        }
        return arr;
    }

    private static void quicksort(int[] arr, int lo, int hi) {
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;     // overflow-safe vs. (lo + hi) / 2
            if (arr[mid] < arr[lo]) swap(arr, lo, mid);
            if (arr[hi]  < arr[lo]) swap(arr, lo, hi);
            if (arr[mid] < arr[hi]) swap(arr, mid, hi);
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

    private static int lomutoPartition(int[] arr, int lo, int hi) {
        int pivot = arr[hi];
        int i = lo - 1;
        for (int j = lo; j < hi; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, hi);
        return i + 1;
    }

    private static void swap(int[] arr, int a, int b) {
        int t = arr[a]; arr[a] = arr[b]; arr[b] = t;
    }
}
