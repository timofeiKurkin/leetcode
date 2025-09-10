function maximumPossibleSize(nums: number[]): number {
    return solution2(nums)
};

function solution1(nums: number[]): number {
    const stack: number[] = []

    for (const num of nums) {
        if (!stack.length) {
            stack.push(num)
        } else if (num - stack[stack.length - 1] < 0) {
            stack[stack.length - 1] = Math.max(stack[stack.length - 1], num)
        } else {
            stack.push(num)
        }
    }

    return stack.length
}

function solution2(nums: number[]): number {
    let length = 1
    let top = nums[0]

    for (const num of nums.slice(1,)) {
        if (top <= num) {
            length += 1
            top = num
        }
    }

    return length
}