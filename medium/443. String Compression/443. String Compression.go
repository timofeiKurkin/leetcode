package main

import "strconv"

func compress(chars []byte) int {
	if len(chars) == 1 {
		return 1
	}

	charsCount := 0
	index := 0

	for index < len(chars) {
		currentChar := chars[index]
		count := 0

		for index < len(chars) && chars[index] == currentChar {
			count += 1
			index += 1
		}

		chars[charsCount] = currentChar
		charsCount += 1

		if count > 1 {
			for _, s := range strconv.Itoa(count) {
				chars[charsCount] = byte(s)
				charsCount += 1
			}
		}
	}

	return charsCount
}
