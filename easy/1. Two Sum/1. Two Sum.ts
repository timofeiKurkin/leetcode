


function twoSum(nums: number[], target: number): number[] {
    return nums.reduce((acc: number[], item, index, array) => {
        const difference = array.indexOf(target - item)

        if (difference > -1 && difference !== index) {
            return [index, difference]
        } else {
            return acc
        }
    }, [])
};

function twoSum2(nums: number[], target: number): number[] {
    const map = new Map<number, number>()

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]

        if (map.has(complement)) {
            return [map.get(complement)!, i]
        }

        map.set(nums[i], i)
    }

    return []
}


console.log(twoSum2([2, 7, 11, 15], 9));
console.log(twoSum2([3, 2, 4], 6));
console.log(twoSum2([3, 3], 6));

