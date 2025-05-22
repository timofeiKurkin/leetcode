package main

func countBitsInNum(num int) int {
	bits := 0
	for num > 0 {
		bits += num & 1
		num /= 2
	}
	return bits
}

func countBits(n int) []int {
	ans := []int{}
	for i := 0; i <= n; i++ {
		ans = append(ans, countBitsInNum(i))
	}
	return ans
}
