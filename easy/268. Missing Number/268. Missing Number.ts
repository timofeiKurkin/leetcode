// Дано: массив чисел, содержащий целочисленные числа в диапазоне [0, n]. Количество чисел ограничено n. Т.е. какая длина массива, то такое наибольшее число в массиве. Но из-за того, что в массиве пропущена одно число, он никогда не будет содержать все числа [0, n] и быть длиной в n элементов.
// Условие: вернуть единственное число, которое пропущено в этом диапазоне.

// Пример 1:
// Input: nums = [3, 0, 1]
// Output: 2
// Explanation: n = 3, поскольку длина массива - 3, поэтому диапазон чисел - [0, 3]. Соответственно число 2 - это пропущенный элемент.

// Пример 2:
// Input: nums = [0,1]
// Output: 2
// Explanation: n = 2, поскольку длина массива - 2, поэтому диапазон чисел - [0, 2]. Соответственно число 2 - это пропущенный элемент.

// Пример 3:
// Input: nums = [9,6,4,2,3,5,7,0,1]
// Output: 8
// Explanation: n = 9, поскольку длина массива - 9, поэтому диапазон чисел - [0, 9]. Соответственно число 8 - это пропущенный элемент.


//Constraints:
// - n == nums.length
// - 1 <= n <= 104
// - 0 <= nums[i] <= n
// - All the numbers of nums are unique.

const num1 = [3,0,1]
const num2 = [0,1]
const num3 = [9,6,4,2,3,5,7,0,1]

function missingNumber(nums: number[]): number {
    // return Array.from(Array(++nums.length).keys()).filter((num) => !nums.includes(num))[0]
    const sortedArr = nums.sort((a, b) => a - b)
    for(let i = 0; i <= sortedArr.length; i++) {
        if (sortedArr[i] === i) continue
        return i
    }
    return 0
};

console.log(missingNumber(num1));
console.log(missingNumber(num2));
console.log(missingNumber(num3));

export {}
