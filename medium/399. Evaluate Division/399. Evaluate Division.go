package main

func isExists(a, b string, graph map[string]map[string]float64) bool {
	if _, ok := graph[a]; !ok {
		return false
	}

	if _, ok := graph[b]; !ok {
		return false
	}

	return true
}

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	graph := make(map[string]map[string]float64)
	seen := make(map[string]bool)

	for i := 0; i < len(equations); i++ {
		a, b := equations[i][0], equations[i][1]

		if _, ok := graph[a]; !ok {
			graph[a] = make(map[string]float64)
		}
		graph[a][b] = values[i]

		if _, ok := graph[b]; !ok {
			graph[b] = make(map[string]float64)
		}
		graph[b][a] = 1 / values[i]
	}

	var divide func(string, string) float64
	divide = func(a, b string) float64 {
		if a == b {
			return 1.0
		}

		seen[a] = true
		for key, value := range graph[a] {
			if seen[key] {
				continue
			}

			res := divide(key, b)
			if res > 0 {
				return res * value
			}
		}

		return -1.0
	}

	ans := make([]float64, 0)
	for _, q := range queries {
		a, b := q[0], q[1]

		if !isExists(a, b, graph) {
			ans = append(ans, -1.0)
			continue
		}

		seen = make(map[string]bool)
		ans = append(ans, divide(a, b))

	}

	return ans
}
