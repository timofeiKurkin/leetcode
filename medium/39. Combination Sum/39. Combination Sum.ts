function combinationSum(candidates: number[], target: number): number[][] {
    const res: number[][] = []
    const n = candidates.length

    const backtrack = (i: number, items: number[], itemsSum: number) => {
        if (i >= n || itemsSum > target)
            return
        if (itemsSum === target) {
            res.push(items)
            return
        }

        // Use duplicate of the current candidate
        const itemsCopy = [...items]
        itemsCopy.push(candidates[i])
        backtrack(i, itemsCopy, itemsSum + candidates[i])

        // Use the next candidate
        backtrack(i + 1, items, itemsSum)
        return
    }

    backtrack(0, [], 0)

    return res
};

export { }

