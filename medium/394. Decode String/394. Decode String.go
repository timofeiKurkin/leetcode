package main

import (
	"strconv"
	"strings"
)

func valueIsNum(value string) bool {
	_, err := strconv.ParseInt(value, 10, 64)
	return err == nil
}

func dfs(i int, s string) (string, int) {
	res := ""

	for i < len(s) {
		if valueIsNum(string(s[i])) {
			k := 0

			for valueIsNum(string(s[i])) {
				num, _ := strconv.ParseInt(string(s[i]), 10, 64)
				k = k*10 + int(num)
				i += 1
			}

			i += 1
			decoded_str, newIndex := dfs(i, s)
			i = newIndex
			res += strings.Repeat(decoded_str, k)
		} else if string(s[i]) == "]" {
			return res, i + 1
		} else {
			res += string(s[i])
			i += 1
		}
	}

	return res, i
}

func decodeString(s string) string {
	res, _ := dfs(0, s)
	return res
}
