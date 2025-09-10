function findJudge(n: number, trust: number[][]): number {
    return solution2(n, trust)
};

function solution1(n: number, trust: number[][]): number {
    if (n == 1) return 1

    const trustGraph: { [key in number]: number[] } = {}
    const trusted = new Set<number>()

    for (const [a, b] of trust) {
        trustGraph[b] = [...trustGraph[b] || [], a]
        trusted.add(a)
    }

    for (const b in trustGraph) {
        if (!trusted.has(Number(b)) && trustGraph[b].length === n - 1) {
            return Number(b)
        }
    }

    return -1
}

function solution2(n: number, trust: number[][]): number {
    const trusted = new Array(n + 1).fill(0)
    const trusts = [...trusted]

    for (const [a, b] of trust) {
        trusted[b] += 1
        trusts[a] += 1
    }

    const judge = trusts.findIndex((item) => item === 0)
    if (judge === -1) return -1
    if (trusted[judge] === n - 1) return judge
    return -1
}

console.log(findJudge(2, [[1, 2]]))
console.log(findJudge(3, [[1, 3], [2, 3]]))
console.log(findJudge(3, [[1, 3], [2, 3], [3, 1]]))
console.log(findJudge(3, [[1, 2], [2, 3]]))