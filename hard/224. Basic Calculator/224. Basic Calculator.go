package main

import (
	"unicode"
)

func calculate(s string) int {
	stack := []int{}
	prevNumber := 0
	result := 0
	sign := 1

	for _, element := range s {
		if unicode.IsDigit(element) {
			prevNumber = prevNumber*10 + int(element-'0')
		} else if element == '+' || element == '-' {
			result += result + sign*prevNumber
			prevNumber = 0

			if element == '+' {
				sign = 1
			} else {
				sign = -1
			}
		} else if element == '(' {
			stack = append(stack, result)
			stack = append(stack, sign)
			result = 0
			sign = 1
		} else if element == ')' {
			result += result + sign*prevNumber
			prevNumber = 0

			result *= stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			result += stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
	}

	result += result + sign*prevNumber
	return result
}
