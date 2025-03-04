function searchInsert(nums: number[], target: number): number {
    const run = (index: number): number => {
        if (!nums.length || index >= nums.length)
            return index

        if (nums.length && (nums[index] >= target || target === nums[index]))
            return index

        return run(index + 1)
    }

    return run(0)
};