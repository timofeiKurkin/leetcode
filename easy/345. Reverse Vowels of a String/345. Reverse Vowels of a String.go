package main

import "strings"

func reverseVowels(s string) string {
	word := []rune(s)
	start := 0
	end := len(word) - 1
	vowels := "aeiouAEIOU"

	for start < end {
		for start < end && !strings.ContainsRune(vowels, word[start]) {
			start += 1
		}
		for start < end && !strings.ContainsRune(vowels, word[end]) {
			end -= 1
		}

		word[start], word[end] = word[end], word[start]
		start += 1
		end -= 1
	}

	return string(word)
}
