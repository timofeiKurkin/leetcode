function countLargestGroup(n: number): number {
    const nums: { [key in number]: number[] } = {}
    let res = 0
    let maxSum = 0

    for (let num = 1; num <= n; num++) {
        const dSum = num > 9 ? num.toString().split("").reduce((acc, curr) => acc + Number(curr), 0) : num

        if (dSum in nums)
            nums[dSum].push(num)
        else
            nums[dSum] = [num]

        const s = nums[dSum].length
        if (s > maxSum) {
            res = 0
            maxSum = s
        } else if (s == maxSum) {
            res += 1
        }
    }

    return res + 1
};