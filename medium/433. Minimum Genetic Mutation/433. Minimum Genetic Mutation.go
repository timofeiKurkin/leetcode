package main

import "fmt"

func minMutation(startGene string, endGene string, bank []string) int {
	bankSet := make(map[string]bool)
	for _, gene := range bank {
		bankSet[gene] = true
	}

	if !bankSet[endGene] {
		return -1
	}

	queue := []string{startGene}
	visited := map[string]bool{startGene: true}
	steps := 0
	genes := []byte{'A', 'C', 'G', 'T'}

	for len(queue) > 0 {
		nextQueue := []string{}

		for _, current := range queue {
			if current == endGene {
				return steps
			}

			for i := 0; i < len(current); i++ {
				for _, g := range genes {
					if current[i] == g {
						continue
					}

					mutated := current[:i] + string(g) + current[i+1:]
					if bankSet[mutated] && !visited[mutated] {
						visited[mutated] = true
						nextQueue = append(nextQueue, mutated)
					}
				}
			}
		}

		queue = nextQueue
		steps++
	}

	return -1
}

func main() {
	fmt.Println(minMutation("AACCGGTT", "AACCGGTA", []string{"AACCGGTA"}))
	fmt.Println(minMutation("AACCGGTT", "AAACGGTA", []string{"AACCGGTA", "AACCGCTA", "AAACGGTA"}))
}
