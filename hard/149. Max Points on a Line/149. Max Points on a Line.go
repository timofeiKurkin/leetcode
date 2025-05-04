package main

import "fmt"

func gcd(a, b int) int {
	if b == 0 {
		return a
	}

	return gcd(b, a%b)
}

func maxPoints(points [][]int) int {
	res := 0
	n := len(points)

	for i := 0; i < n; i++ {
		hash := make(map[[2]int]int)
		maxCount := 0
		samePoint := 0
		x1, y1 := points[i][0], points[i][1]

		for j := 0; j < n; j++ {
			if i == j {
				samePoint += 1
				continue
			}

			x2, y2 := points[j][0], points[j][1]
			dx := x2 - x1
			dy := y2 - y1

			if dx == 0 && dy == 0 {
				samePoint += 1
			} else {
				g := gcd(dx, dy)
				dx /= g
				dy /= g

				if dx < 0 {
					dx = -dx
					dy = -dy
				}

				slope := [2]int{dy, dx}
				hash[slope] += 1

				if hash[slope] > maxCount {
					maxCount = hash[slope]
				}
			}
		}

		res = max(res, maxCount+samePoint)
	}

	return res
}

func main() {
	// [2]int{}
	fmt.Println(maxPoints([][]int{{1, 1}, {2, 2}, {3, 3}}))
	fmt.Println(maxPoints([][]int{{1, 1}, {3, 2}, {5, 3}, {4, 1}, {2, 3}, {1, 4}}))
}
