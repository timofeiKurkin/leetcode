package main

func maxOperations(nums []int, k int) int {
	// sort.Ints(nums)

	// end := len(nums) - 1
	// start := 0
	// res := 0

	// for start < end {
	// 	if nums[start] == k {
	// 		start += 1
	// 	} else if nums[end] == k {
	// 		end -= 1
	// 	} else {
	// 		if nums[start]+nums[end] == k {
	// 			res += 1
	// 			start += 1
	// 			end -= 1
	// 		} else {
	// 			if k-nums[end] >= nums[start] {
	// 				start += 1
	// 			} else {
	// 				end -= 1
	// 			}
	// 		}
	// 	}
	// }

	// return res

	pairs := make(map[int]int)
	ops := 0

	for _, n := range nums {
		value, ok := pairs[k-n]
		if !ok || value < 1 {
			pairs[n]++
			continue
		}
		ops += 1
		pairs[k-n] -= 1
	}

	return ops
}
