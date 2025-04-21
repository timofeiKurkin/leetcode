function minMutation(startGene: string, endGene: string, bank: string[]): number {
    const bankSet = new Set(bank)

    if (!bankSet.has(endGene)) return -1

    let queue: string[] = [startGene]
    const visited = new Set([startGene])
    let steps = 0
    const genes = ["A", "C", "G", "T"]

    while (queue.length > 0) {
        const nextQueue: string[] = []

        for (const current of queue) {
            if (current == endGene) return steps

            for (let i = 0; i < current.length; i++) {
                for (const gene of genes) {
                    if (current[i] === gene) continue

                    const mutated = current.slice(0, i) + gene + current.slice(i + 1,)
                    if (bankSet.has(mutated) && !visited.has(mutated)) {
                        visited.add(mutated)
                        nextQueue.push(mutated)
                    }
                }
            }
        }

        queue = nextQueue
        steps += 1
    }

    return -1
};

console.log(minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
console.log(minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))

export { }

