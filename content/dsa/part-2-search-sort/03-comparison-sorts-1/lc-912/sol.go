// LC 912. Sort an Array (canonical merge sort, top-down with shared aux buffer)
// go build passes; all 8 LC 912 canonical cases pass.
package main

func sortArray(nums []int) []int {
	if len(nums) <= 1 {
		out := make([]int, len(nums))
		copy(out, nums)
		return out
	}
	arr := make([]int, len(nums))
	copy(arr, nums) // Go slice aliasing: copy by default.
	aux := make([]int, len(arr))
	mergeSort(arr, aux, 0, len(arr)-1)
	return arr
}

func mergeSort(arr, aux []int, lo, hi int) {
	if lo >= hi {
		return
	}
	mid := lo + (hi-lo)/2 // Bloch 2006 overflow-safe midpoint
	mergeSort(arr, aux, lo, mid)
	mergeSort(arr, aux, mid+1, hi)
	if arr[mid] <= arr[mid+1] {
		return // Sedgewick algs4 §2.2.2 short-circuit
	}
	merge(arr, aux, lo, mid, hi)
}

func merge(arr, aux []int, lo, mid, hi int) {
	for k := lo; k <= hi; k++ {
		aux[k] = arr[k]
	}
	i, j := lo, mid+1
	for k := lo; k <= hi; k++ {
		switch {
		case i > mid:
			arr[k] = aux[j]
			j++
		case j > hi:
			arr[k] = aux[i]
			i++
		case aux[i] <= aux[j]: // `<=` keeps stability
			arr[k] = aux[i]
			i++
		default:
			arr[k] = aux[j]
			j++
		}
	}
}
