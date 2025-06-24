function findKDistantIndices(nums: number[], key: number, k: number): number[] {
    const res: number[] = []
    const n = nums.length
    let r = 0

    for (let j = 0; j < n; j++) {
        if (nums[j] === key) {
            const l = Math.max(r, j - k)
            r = Math.min(n - 1, j + k) + 1

            for (let i = l; i < r; i++)
                res.push(i)
        }
    }

    return res
};