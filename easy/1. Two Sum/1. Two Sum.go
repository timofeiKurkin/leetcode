package main

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		diff := target - nums[i]

		if _, ok := seen[diff]; ok {
			return []int{seen[diff], i}
		}

		seen[diff] = i
	}

	return []int{}
}
