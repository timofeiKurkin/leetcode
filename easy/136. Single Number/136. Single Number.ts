// 136. Single Numbers
// Дано:  не пустой массив чисел. Каждое число, кроме одного, повторяется дважды.
// Условие: вернуть число, которое не повторяется единожды
// Вы должны реализовать решение с линейной сложностью времени выполнения и использовать только постоянное дополнительное пространство.

// Пример 1:
// Вход: nums = [2,2,1]
// Выход: 1

// Пример 2:
// Вход: nums = nums = [4,1,2,1,2]
// Выход: 4

// Пример 3:
// Вход: nums = [1]
// Выход: 1

const nums1 = [2, 2, 1]
const nums2 = [4, 1, 2, 1, 2]
const nums3 = [1]


function singleNumber(nums: number[]): number {
    // Runtime: 67ms
    // const map = new Map()
    // for (let i = 0; i <= nums.length; i++) {
    //     if(map.has(nums[i])) map.delete(nums[i])
    //     else map.set(nums[i], nums[i])
    // }
    // nums = [...map.keys()]
    // return nums[0]

    // Runtime: 62ms
    let res = 0
    for (let num of nums) {
        res ^= num
    }
    return res
};

// console.log(singleNumber(nums1));
console.log(singleNumber(nums2));
// console.log(singleNumber(nums3));

export { }