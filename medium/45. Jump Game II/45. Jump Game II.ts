function jump(nums: number[]): number {
    let jumps = 0
    let reachable = 0
    let end = 0

    for (let i = 0; i < nums.length - 1; i++) {
        reachable = Math.max(reachable, nums[i] + i)

        if (end === i) {
            end = reachable
            jumps += 1
        }

        if (end >= nums.length - 1)
            break
    }

    return jumps
};