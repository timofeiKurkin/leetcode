package main

func removeStars(s string) string {
	res := []byte{}

	for i := 0; i < len(s); i++ {
		if s[i] != '*' {
			res = append(res, s[i])
		} else {
			res = res[:len(res)-1]
		}
	}

	return string(res)
}
