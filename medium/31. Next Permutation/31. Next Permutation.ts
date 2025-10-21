/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void {
    let i = nums.length - 1
    while (i > 0 && nums[i - 1] >= nums[i]) {
        i -= 1
    }

    if (!i) {
        nums.reverse()
        return
    }

    let j = nums.length - 1
    while (j >= i && nums[j] <= nums[i - 1]) {
        j -= 1
    }

    const reverse = (nums: number[], start: number, end: number) => {
        while (start < end) {
            [nums[start], nums[end]] = [nums[end], nums[start]];
            start++;
            end--;
        }
    }
    [nums[i - 1], nums[j]] = [nums[j], nums[i - 1]]
    reverse(nums, i, nums.length - 1)
};
