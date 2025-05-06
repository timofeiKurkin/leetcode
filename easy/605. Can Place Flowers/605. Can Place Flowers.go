package main

import "slices"

func canPlaceFlowers(flowerbed []int, n int) bool {
	flowerbed = append([]int{0}, append(flowerbed, 0)...)

	for i := 1; i < len(flowerbed)-1; i++ {
		if slices.Equal(flowerbed[i-1:i+2], []int{0, 0, 0}) {
			flowerbed[i] = 1
			n -= 1
			if n == 0 {
				return true
			}
		}
	}

	return n <= 0

}
