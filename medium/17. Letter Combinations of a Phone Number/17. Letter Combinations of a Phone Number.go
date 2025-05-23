package main

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}

	res := []string{}
	phone_keyboard := map[string][]string{
		"2": {"a", "b", "c"},
		"3": {"d", "e", "f"},
		"4": {"g", "h", "i"},
		"5": {"j", "k", "l"},
		"6": {"m", "n", "o"},
		"7": {"p", "q", "r", "s"},
		"8": {"t", "u", "v"},
		"9": {"w", "x", "y", "z"},
	}

	var backtrack func(index int, combination string)

	backtrack = func(index int, combination string) {
		if index == len(digits) {
			res = append(res, combination)
			return
		}

		digit := string(digits[index])
		for _, letter := range phone_keyboard[digit] {
			backtrack(index+1, combination+letter)
		}
	}

	backtrack(0, "")
	return res
}
