// Дано: массив целочисленных чисел nums, где nums[i] находится в диапазоне значений [1, n]. Элементы массива могут повторяться, чтобы заполнить отсутствующие элементы.
// Условие: вернуть массив чисел диапазона [1, n], которые не встречаются в nums.

// Пример 1:
// Вход: nums = [4,3,2,7,8,2,3,1]
// Выход: [5, 6]

// Пример 2:
// Вход: nums = [1,1]
// Выход: [2]

// Ограничения:
// * n == nums.length - самое большое число равно длине массива
// * 1 <= n <= 10^5
// * 1 <= nums[i] <= n

// Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
// В этом контексте речь идет о задаче, в которой требуется выполнить операцию за линейное время — O(n) — и не использовать дополнительную память, за исключением возвращаемого списка. Алгоритм должен изменять входной массив "на месте" (in-place).

const nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
const nums2 = [1, 1]

function findDisappearedNumbers(nums: number[]): number[] {
    // nums.sort((a, b) => a - b)
    // const result = []
    // for(let i = 1; i <= nums.length; i++) {
    //     if(nums.includes(i)) continue
    //     result.push(i)
    // }
    // return result

    // return Array.from(Array(++nums.length).keys()).filter(num => num && !nums.includes(num))

    for (let i = 0; i < nums.length; i++) {
        const index = Math.abs(nums[i]) - 1
        nums[index] = -Math.abs(nums[index])
    }

    const res: number[] = []

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 0) res.push(i + 1)
    }

    return res
};


console.log(findDisappearedNumbers(nums1));
console.log(findDisappearedNumbers(nums2));


export {}