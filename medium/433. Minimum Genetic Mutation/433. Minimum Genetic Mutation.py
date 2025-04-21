from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = {gene: True for gene in bank}

        if endGene not in bank_set:
            return -1

        queue: List[str] = [startGene]
        visited = {startGene: True}
        steps = 0
        genes = {"A", "C", "G", "T"}

        while len(queue) > 0:
            next_queue: List[str] = []

            for current in queue:
                if current == endGene:
                    return steps

                for i in range(len(current)):
                    for g in genes:
                        if current[i] == g:
                            continue

                        mutated = current[:i] + g + current[i + 1 :]
                        if (
                            mutated in bank_set
                            and bank_set[mutated]
                            and mutated not in visited
                        ):
                            visited[mutated] = True
                            next_queue.append(mutated)

            queue = next_queue
            steps += 1

        return -1


solution = Solution()
print(solution.minMutation(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"]))
print(
    solution.minMutation(
        startGene="AACCGGTT",
        endGene="AAACGGTA",
        bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"],
    )
)
