function subsets(nums: number[]): number[][] {
    const res: number[][] = []

    const backtrack = (path: number[], arr: number[]) => {
        res.push(path)

        if (!res.length) return
        for (let i = 0; i < arr.length; i++) {
            backtrack(path.concat([arr[i]]), arr.slice(i + 1,))
        }
    }

    backtrack([], nums)

    return res
};