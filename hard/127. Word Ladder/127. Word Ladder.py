from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words_graph = set(wordList)  # {word: False for word in wordList}

        if endWord not in words_graph:
            return 0

        res = 1
        queue = [beginWord]
        visited = set([beginWord])
        genes = set()
        for s in wordList:
            for k in s:
                genes.add(k)

        answers = []

        while queue:
            next_queue = []

            for current in queue:
                if current == endWord:
                    answers.append(res)

                for i in range(len(current)):
                    for g in genes:
                        if current[i] == g:
                            continue

                        mutated = current[:i] + g + current[i + 1 :]
                        if mutated in words_graph and mutated not in visited:
                            next_queue.append(mutated)
                            visited.add(mutated)

            queue = next_queue
            res += 1

        return min(answers)


solution = Solution()
print(
    solution.ladderLength(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"],
    )
)
