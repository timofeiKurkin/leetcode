const arr1 = [40, 10, 20, 30]
const arr2 = [100, 100, 100]
const arr3 = [37, 12, 28, 9, 100, 56, 80, 5, 12]
const arr4 = [-5, 6, 5, -44, 27, 14, -27, 36, -17, -6, 13, -12]

// [40,10,20,30]
// [4, 1, 2, 3]

// GIVEN: array with numbers
// FOUND: the rank of each number
// CONDITIONS:
// - Rank is an integer starting from 1.
// - The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
// - Rank should be as small as possible.

// Example 1:
// Input: arr = [40,10,20,30]
// Output: [4,1,2,3]
// Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

// Ограничения:
// - Максимальный ранг <= длина исходного массива
// 

// Алгоритм:
// - Отсортировать массив по возрастанию: [5, 9, 12, 12, 28, 37, 56, 80, 100]
// - 

function arrayRankTransform(arr: number[]): number[] {
    let rank = 1
    const result = new Array(arr.length)
    const sortedArr = arr.map((item, index) => ([item, index])).sort((a, b) => a[0] - b[0])

    for (let i = 0; i < sortedArr.length; i++) {
        if (i !== sortedArr.length - 1 && sortedArr[i][0] === sortedArr[i + 1][0]) {
            result[sortedArr[i][1]] = rank
            continue
        } else if (i > 0 && sortedArr[i][0] === sortedArr[i - 1][0]) {
            result[sortedArr[i][1]] = rank
            rank++
            continue
        }

        result[sortedArr[i][1]] = rank
        rank++
    }

    return result
};

function arrayRankTransform2(arr: number[]): number[] {
    const sortedArr = [...arr].sort((a, b) => a - b);
    const rankMap = new Map();
    let rank = 1;

    for (let i = 0; i < sortedArr.length; i++) {
        if (!rankMap.has(sortedArr[i])) {
            rankMap.set(sortedArr[i], rank);
            rank++;
        }
    }

    return arr.map(num => rankMap.get(num));
}

console.log(arrayRankTransform(arr1));
console.log(arrayRankTransform(arr2));
console.log(arrayRankTransform(arr3));
console.log(arrayRankTransform(arr4));

// console.log(arrayRankTransform2(arr1));
// console.log(arrayRankTransform2(arr2));
// console.log(arrayRankTransform2(arr3));
// console.log(arrayRankTransform2(arr4));