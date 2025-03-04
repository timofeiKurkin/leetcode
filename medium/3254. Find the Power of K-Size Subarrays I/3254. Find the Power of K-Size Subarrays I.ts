function resultsArray(nums: number[], k: number): number[] {
    if (nums.length < k) return []

    function checkPower(start: number): boolean {
        for (let i = start; i < start + k - 1; i++) {
            if (nums[i + 1] - nums[i] != 1) return false
        }
        return true
    }

    function computeResults(index: number): number[] {
        if (index + k > nums.length) return []
        const isPower = checkPower(index)
        const maxNum = isPower ? nums[index + k - 1] : -1;
        return [maxNum, ...computeResults(index + 1)]
    }

    return computeResults(0)
};


// function check_power(nums: number[]): boolean {
//     for (let i = 0; i < nums.length; i++) {
//         if (nums[i + 1] - nums[i] != 1) return false
//     }
//     return true
// }

