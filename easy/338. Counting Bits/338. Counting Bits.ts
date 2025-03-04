// 338. Counting Bits
// Дано: число n.
// Условие: верните массив с длиной n + 1, где каждый элемент i (0 <= i <= n) представляет собой сумму его двоичного представления или же количество 1 в его двоичном представлении. 

// Пример 1:
// Вход: n = 2
// Выход: [0, 1, 1]
// Объяснение:
// 0 --> 0
// 1 --> 1
// 2 --> 10

// Пример 2:
// Вход: n = 5
// Выход: [0,1,1,2,1,2]
// Объяснение:
// 0 --> 0
// 1 --> 1
// 2 --> 10 = 1
// 3 --> 11 = 2
// 4 --> 100 = 1
// 5 --> 101 = 2
// 6 --> 110 = 2
// 7 --> 111 = 3
// 8 --> 1000 = 1

const n1 = 2
const n2 = 5
const n3 = 12
const n4 = 103
const n5 = 1723
const n6 = Math.pow(10, 5)

function checkNumIsEven(i: number): number {
    if (i % 2 !== 0) return 1
    return 0
}

function countBits(n: number): number[] {
    const resArr: number[] = new Array(n + 1).fill(0)

    for (let i = 0; i < resArr.length; i++) {
        resArr[i] = resArr[i >> 1] + checkNumIsEven(i)
    }

    return resArr
};

console.log(countBits(n1));
console.log(countBits(n2));
console.log(countBits(n3));
// console.log(countBits(n4));
// console.log(countBits(n5));
// console.log(countBits(n6));

