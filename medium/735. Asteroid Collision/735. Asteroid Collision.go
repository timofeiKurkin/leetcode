package main

func asteroidCollision(asteroids []int) []int {
	stack := []int{}

	for _, ast := range asteroids {
		if len(stack) < 0 || ast > 0 {
			stack = append(stack, ast)
		} else {
			for len(stack) > 0 && ast != 0 && stack[len(stack)-1] > 0 {
				if ast+stack[len(stack)-1] == 0 {
					ast = 0
					stack = stack[:len(stack)-1]
					break
				} else if ast+stack[len(stack)-1] < 0 {
					stack = stack[:len(stack)-1]
				} else if stack[len(stack)-1]+ast > 0 {
					ast = 0
					break
				}
			}

			if ast != 0 && (len(stack) < 0 || (len(stack) > 0 && stack[len(stack)-1] < 0)) {
				stack = append(stack, ast)
			}
		}
	}

	return stack
}
