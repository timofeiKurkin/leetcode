function intersection(nums: number[][]): number[] {
    return solution2(nums)
};

function solution1(nums: number[][]): number[] {
    const n = nums.length
    const ht: { [key in number]: number } = {}

    for (const subArray of nums) {
        for (const num of subArray) {
            ht[num] = (ht[num] || 0) + 1
        }
    }

    const res: number[] = []

    for (const num in ht) {
        if (ht[num] === n) {
            res.push(Number(num))
        }
    }

    return res
}


function solution2(nums: number[][]): number[] {
    if (nums.length === 1) return nums[0].sort((a, b) => a - b)

    let res = new Set(nums[0])
    for (let i = 1; i < nums.length; i++) {
        res = new Set([...nums[i]].filter(x => res.has(x)))
    }

    return Array.from(res.values()).sort((a, b) => a - b)
}