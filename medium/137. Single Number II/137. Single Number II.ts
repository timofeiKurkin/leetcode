function singleNumber(nums: number[]): number {
    const myMap = new Map()

    for (let i = 0; i < nums.length; i++) {
        if (myMap.has(nums[i])) {
            myMap.set(nums[i], myMap.get(nums[i]) + 1)
        } else {
            myMap.set(nums[i], 1)
        }
    }

    for (let [key, item] of myMap) {
        if (item === 1) return key
    }
    return 0
};


console.log(singleNumber([0, 1, 0, 1, 0, 1, 99]));

