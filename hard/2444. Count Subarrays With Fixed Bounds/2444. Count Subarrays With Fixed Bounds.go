package main

func countSubarrays(nums []int, minK int, maxK int) int64 {
	n := len(nums)
	worst := -1
	minIndex := -1
	maxIndex := -1

	res := 0

	for i := 0; i < n; i++ {
		if nums[i] < minK || nums[i] > maxK {
			worst = i
		}

		if nums[i] == minK {
			minIndex = i
		}

		if nums[i] == maxK {
			maxIndex = i
		}

		res += max(0, min(minIndex, maxIndex)-worst)
	}

	return int64(res)
}
