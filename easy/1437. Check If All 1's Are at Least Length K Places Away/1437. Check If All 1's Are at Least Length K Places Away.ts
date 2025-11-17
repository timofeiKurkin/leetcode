function kLengthApart(nums: number[], k: number): boolean {
    return solution1(nums, k)
};

function solution1(nums: number[], k: number): boolean {
    let i = 0

    while (nums.length && !nums[nums.length - 1]) {
        nums.pop()
    }

    while (i < nums.length) {

        if (!nums[i]) {
            i += 1
        } else {
            let j = i + 1

            if (j >= nums.length) {
                break
            }

            while (j < nums.length && !nums[j]) {
                j += 1
            }

            if ((j - i - 1) < k) {
                return false
            }

            i = j
        }
    }

    return true
}

function solution2(nums: number[], k: number): boolean {
    let counter = 0, isFirst = true

    for (let i = 0; i < nums.length; i++) {
        if (nums[i]) {
            if (counter < k && !isFirst) {
                return false
            }
            counter = 0
            isFirst = false
        } else {
            counter += 1
        }
    }

    return true
}