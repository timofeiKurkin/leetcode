// Дано: массив целочисленных чисел
// Необходимо: вернуть true, если какое-то из чисел массива повторяется более одного раза. И вернуть false, если каждое число уникальное.

// Example 1:
// Input: nums = [1,2,3,1]
// Output: true
// Explanation:
// The element 1 occurs at the indices 0 and 3.

// Example 2:
// Input: nums = [1,2,3,4]
// Output: false
// Explanation:
// All elements are distinct.

// Example 3:
// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true

// Решения:
// 1. Создать new Map и складывать туда числа исходного массива. Как только попадется повторное значение, вернуть true
// 2. Пройтись по массиву, и для каждого элемента использовать .indexOf() по исходному массиву. Если значение != -1, то вернуть false (значение не найдено), в обратном случае вернуть true.

// Cases:
const nums1 = [1, 2, 3, 1]
const nums2 = [1, 2, 3, 4]
const nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

function containsDuplicate(nums: number[]): boolean {
    const map = new Map()
    let status = false

    for (let i = 0; i < nums.length; i++) {
        if (!map.has(nums[i])) {
            map.set(nums[i], 1)
        } else {
            status = true
            break
        }
    }

    return status
};


console.log(containsDuplicate(nums1));
console.log(containsDuplicate(nums2));
console.log(containsDuplicate(nums3));

export {}
