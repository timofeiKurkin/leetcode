package main

import "math"

func divide(dividend int, divisor int) int {
	if dividend == math.MinInt32 && divisor == -1 {
		return math.MaxInt32
	}

	sign := 1
	if dividend*divisor < 0 {
		sign = -1
	}

	a := int(math.Abs(float64(dividend)))
	b := int(math.Abs(float64(divisor)))
	res := 0

	for a-b >= 0 {
		x := 0
		for a-(b<<1<<x) >= 0 {
			x += 1
		}

		res += 1 << x
		a -= b << x
	}

	return res * sign
}
