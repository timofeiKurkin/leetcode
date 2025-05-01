package main

import "fmt"

func ladderLength(beginWord string, endWord string, wordList []string) int {
	wordSet := make(map[string]bool)
	for _, w := range wordList {
		wordSet[w] = true
	}

	if _, exists := wordSet[endWord]; !exists {
		return 0
	}

	res := 1
	wordQueue := []string{beginWord}

	for len(wordQueue) > 0 {
		levelSize := len(wordQueue)

		for i := 0; i < levelSize; i++ {
			curr := wordQueue[0]
			if curr == endWord {
				return res
			}

			wordQueue = wordQueue[1:]

			for j := 0; j < len(curr); j++ {
				for c := 'a'; c <= 'z'; c++ {
					if byte(c) == curr[j] {
						continue
					}

					mutated := curr[:j] + string(c) + curr[j+1:]
					if _, exists := wordSet[mutated]; exists {
						wordQueue = append(wordQueue, mutated)
						delete(wordSet, mutated)
					}

				}
			}
		}

		res += 1
	}

	return 0
}

func main() {
	fmt.Println(ladderLength("hit", "cog", []string{"hot", "dot", "dog", "lot", "log", "cog"}))
}
