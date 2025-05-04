package main

func normalizeKey(a, b int) [2]int {
	if a < b {
		return [2]int{a, b}
	}
	return [2]int{b, a}
}

func numEquivDominoPairs(dominoes [][]int) int {
	n := len(dominoes)
	if n == 1 {
		return 0
	}

	hash := make(map[[2]int]int)
	for i := 0; i < n; i++ {
		domino := normalizeKey(dominoes[i][0], dominoes[i][1])
		hash[domino] += 1
	}

	res := 0

	for _, v := range hash {
		res += v * (v - 1) / 2
	}

	return res
}

func main() {

}
