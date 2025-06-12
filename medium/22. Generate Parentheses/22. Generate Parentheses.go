package main

func generateParenthesis(n int) []string {
	res := []string{}
	o, c := "(", ")"

	var backtrack func(path string, opened, closed int)
	backtrack = func(path string, opened, closed int) {
		if len(path) == n*2 {
			res = append(res, path)
			return
		}

		if opened < n {
			backtrack(path+o, opened+1, closed)
		}
		if closed < n {
			backtrack(path+c, opened, closed+1)
		}

		return
	}

	backtrack("", 0, 0)

	return res
}
