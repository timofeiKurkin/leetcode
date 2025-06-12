package main

func combinationSum(candidates []int, target int) [][]int {
	res := [][]int{}
	n := len(candidates)

	var backtrack func(i, currSum int, items []int)
	backtrack = func(i, total int, items []int) {
		if i >= n || total > target {
			return
		}

		if total == target {
			res = append(res, items)
			return
		}

		// Add current num to total sum
		itemsCopy := append(append([]int{}, items...), candidates[i])
		backtrack(i, total+candidates[i], itemsCopy)

		// Or skip this num and go on
		backtrack(i+1, total, items)
		return
	}

	backtrack(0, 0, []int{})

	return res
}
