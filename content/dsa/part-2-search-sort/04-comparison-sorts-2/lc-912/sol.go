// LC 912. Sort an Array
// Quicksort with median-of-three Lomuto partition.
package main

func sortArray(nums []int) []int {
	arr := append([]int(nil), nums...)
	if len(arr) > 1 {
		quicksort(arr, 0, len(arr)-1)
	}
	return arr
}

func quicksort(arr []int, lo, hi int) {
	for lo < hi {
		mid := lo + (hi-lo)/2
		if arr[mid] < arr[lo] {
			arr[lo], arr[mid] = arr[mid], arr[lo]
		}
		if arr[hi] < arr[lo] {
			arr[lo], arr[hi] = arr[hi], arr[lo]
		}
		if arr[mid] < arr[hi] {
			arr[mid], arr[hi] = arr[hi], arr[mid]
		}
		p := lomutoPartition(arr, lo, hi)
		if p-lo < hi-p {
			quicksort(arr, lo, p-1)
			lo = p + 1
		} else {
			quicksort(arr, p+1, hi)
			hi = p - 1
		}
	}
}

func lomutoPartition(arr []int, lo, hi int) int {
	pivot := arr[hi]
	i := lo - 1
	for j := lo; j < hi; j++ {
		if arr[j] <= pivot {
			i++
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
	arr[i+1], arr[hi] = arr[hi], arr[i+1]
	return i + 1
}
