package main

func findDifference(nums1 []int, nums2 []int) [][]int {
	items1 := make(map[int]bool)
	items2 := make(map[int]bool)

	for _, num := range nums1 {
		items1[num] = true
	}

	for _, num := range nums2 {
		items2[num] = true
	}

	ans := make([][]int, 2)

	for i := range items2 {
		if !items1[i] {
			ans[1] = append(ans[1], i)
		}
	}

	for i := range items1 {
		if !items2[i] {
			ans[0] = append(ans[0], i)
		}
	}

	return ans
}
