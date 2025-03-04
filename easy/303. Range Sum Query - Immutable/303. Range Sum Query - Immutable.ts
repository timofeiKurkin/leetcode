// 303. Range Sum Query - Immutable
// Дан массив чисел nums. А также массив других чисел, представляющие из себя индексы исходного массива - [left, right]. Левый индекс всегда меньше чем правый.
// Условие: Нужно взять все числа между индексами [left, right] и сложить их. Полученную сумму нужно вернуть как результат.

// Пример 1:
// Вход: "NumArray", "sumRange", "sumRange", "sumRange"]
// [[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
// Выход: [null, 1, -1, -3]
// Пояснение:
// NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
// numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
// numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
// numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


const example1 = [-2, 0, 3, -5, 2, -1]


class NumArray {
    nums: number[]

    constructor(nums: number[]) {
        this.nums = nums
    }

    sumRange(left: number, right: number): number {
        // return this.nums.slice(left, right + 1).reduce((a, b) => a + b, 0)

        // let res = 0
        // for (let i = 0; i <= right; i++) {
        //     if (i >= left && i <= right) res += this.nums[i]
        //     else if (i > right) break
        //     else continue
        // }
        // return res

        let res = 0
        for (let i = left; i <= right; i++) {
            res += this.nums[i]
        }
        return res
    }
}

const obj = new NumArray(example1)
console.log(obj.sumRange(0, 2));
console.log(obj.sumRange(2, 5));
console.log(obj.sumRange(0, 5));


export { }