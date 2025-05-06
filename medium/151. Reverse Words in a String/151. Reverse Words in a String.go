package main

import (
	"strings"
)

func reverse(arr []string) {
	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		arr[i], arr[j] = arr[j], arr[i]
	}
}

func standardizeSpaces(s string) string {
	normalized := strings.Fields(s)
	reverse(normalized)
	return strings.Join(normalized, " ")
}

func reverseWords(s string) string {
	return standardizeSpaces(s)
}
