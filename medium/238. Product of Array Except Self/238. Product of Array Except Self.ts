function productExceptSelf(nums: number[]): number[] {
    const n = nums.length
    let answer: number[] = new Array(n).fill(1)

    let prefix = 1
    for (let i = 0; i < n; i++) {
        answer[i] = prefix
        prefix *= nums[i]
    }

    let suffix = 1
    for (let i = n - 1; i >= 0; i--) {
        answer[i] *= suffix
        suffix *= nums[i]
    }

    return answer
};


console.log(productExceptSelf([1, 2, 3, 4]))
