/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
    const n = nums.length
    k %= n

    const rotated = nums.slice(-k,).concat(nums.slice(0, -k))

    for (let i = 0; i < n; i++) {
        nums[i] = rotated[i]
    }

    console.log(nums)
};


const case1 = [1, 2, 3, 4, 5, 6, 7]
const case2 = [-1, -100, 3, 99]
const case3 = [1, 2]
const case4 = [1, 2, 3]
const case5 = [1, 2, 3]


rotate(case1, 3)
rotate(case2, 2)
rotate(case3, 3)
rotate(case4, 0)
rotate(case5, 2)