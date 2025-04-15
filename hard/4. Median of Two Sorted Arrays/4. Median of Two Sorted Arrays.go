package main

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	i := 0
	j := 0

	first := 0
	second := 0

	n := len(nums1) + len(nums2)
	middle := n / 2

	for p := 0; p <= int(middle); p++ {
		first = second

		if i < len(nums1) && (j >= len(nums2) || nums1[i] < nums2[j]) {
			second = nums1[i]
			i += 1
		} else {
			second = nums2[j]
			j += 1
		}
	}

	if n%2 == 0 {
		return float64((first + second) / 2)
	}

	return float64(second)
}
