// LC 912. Sort an Array (canonical merge sort, top-down with shared aux buffer)
class Sol {
    public int[] sortArray(int[] nums) {
        if (nums.length <= 1) return nums.clone();
        int[] arr = nums.clone();
        int[] aux = new int[arr.length];   // shared scratch buffer
        mergeSort(arr, aux, 0, arr.length - 1);
        return arr;
    }

    private void mergeSort(int[] arr, int[] aux, int lo, int hi) {
        if (lo >= hi) return;
        int mid = lo + (hi - lo) / 2;       // Bloch 2006 overflow-safe midpoint
        mergeSort(arr, aux, lo, mid);
        mergeSort(arr, aux, mid + 1, hi);
        if (arr[mid] <= arr[mid + 1]) return;   // Sedgewick algs4 §2.2.2 short-circuit
        merge(arr, aux, lo, mid, hi);
    }

    private void merge(int[] arr, int[] aux, int lo, int mid, int hi) {
        for (int k = lo; k <= hi; k++) aux[k] = arr[k];
        int i = lo, j = mid + 1;
        for (int k = lo; k <= hi; k++) {
            if (i > mid)               arr[k] = aux[j++];
            else if (j > hi)           arr[k] = aux[i++];
            else if (aux[i] <= aux[j]) arr[k] = aux[i++];   // `<=` keeps stability
            else                       arr[k] = aux[j++];
        }
    }
}
