package main

func predictPartyVictory(senate string) string {
	rItems := []int{}
	dItems := []int{}
	n := len(senate)

	for i := 0; i < n; i++ {
		if senate[i] == 'R' {
			rItems = append(rItems, i)
		} else {
			dItems = append(dItems, i)
		}
	}

	for len(rItems) > 0 && len(dItems) > 0 {
		r := rItems[0]
		rItems = rItems[1:]

		d := dItems[0]
		dItems = dItems[1:]

		if r < d {
			rItems = append(rItems, n+r)
		} else {
			dItems = append(dItems, n+d)
		}
	}

	if len(rItems) > 0 {
		return "Radiant"
	} else {
		return "Dire"
	}
}
