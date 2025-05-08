package main

func maxArea(height []int) int {
	amount := 0

	first, second := 0, len(height)-1

	for first < second {
		boundaries := min(height[first], height[second])
		weight := len(height) - (first + second)
		amount = max(amount, boundaries*weight)

		if height[first] <= height[second] {
			first += 1
		} else {
			second -= 1
		}
	}

	return amount
}
