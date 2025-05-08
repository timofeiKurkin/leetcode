package main

func isSubsequence(s string, t string) bool {
	if len(s) == 0 {
		return true
	}

	if len(t) == 0 {
		return false
	}

	first := 0

	for second := 0; second < len(t); second++ {
        if first == len(s) {
            return true
        }
        
		if t[second] == s[first] {
			first += 1
		}
	}

	return first == len(s)
}

