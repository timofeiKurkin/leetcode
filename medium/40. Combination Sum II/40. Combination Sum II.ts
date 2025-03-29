function combinationSum2(candidates: number[], target: number): number[][] {
    const res: number[][] = []
    const n = candidates.length
    candidates = candidates.sort((a, b) => a - b)

    const backtrack = (i: number, nums: number[], remaining: number) => {
        if (!remaining) {
            res.push([...nums])
            return
        }

        for (let j = i; j < n; j++) {
            const curr = candidates[j]
            if (j > i && curr === candidates[j - 1])
                continue

            if (curr > remaining)
                break

            nums.push(curr)
            backtrack(j + 1, nums, remaining - curr)
            nums.pop()
        }
    }

    backtrack(0, [], target)

    return res
};

console.log(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))


export { }

