package main

func scoreOfString(s string) int {
	res := 0

	

	for i := 0; i < len(s)-1; i++ {
		score := int(s[i]) - int(s[i])
		res += max(score, -score)
	}

	return res
}
