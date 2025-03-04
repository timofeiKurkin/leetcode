// 12. Integer to Roman
// Дано: целочисленное число от 0 до 3999
// Условие: вернуть это число римском представлении

// Пример 1
// Вход: num = 3749
// Выход: "MMMDCCXLIX"
// Объяснение: 3000 = MMM; 700 = DCC; 40 = XL; 9 = IX


const int1 = 3749 // MMMDCCXLIX
const int2 = 58 // LVIII
const int3 = 1994 // MCMXCIV

const intNums: { [key: number]: string } = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}

function intToRoman(num: number): string {
    // let roman = ""
    // const nums = num.toString().split("").reverse()

    // for (let i = 0; i < nums.length; i++) {
    //     const discharge = 10 ** i || 1
    //     const itemN = Number(nums[i])

    //     if (itemN === 4 || itemN === 9) {
    //         roman = `${intNums[discharge]}${intNums[(itemN + 1) * discharge]}` + roman
    //     } else {
    //         if (itemN === 1 || itemN === 5) {
    //             roman = intNums[itemN * discharge] + roman
    //         } else {
    //             if (itemN > 5) {
    //                 roman = intNums[5 * discharge] + intNums[discharge].repeat(itemN - 5) + roman
    //             } else {
    //                 roman = intNums[discharge].repeat(itemN) + roman
    //             }
    //         }
    //     }
    // }

    // return roman

    const valueMap: [number, string][] = [
        [1000, "M"], [900, "CM"], [500, "D"], [400, "CD"],
        [100, "C"], [90, "XC"], [50, "L"], [40, "XL"],
        [10, "X"], [9, "IX"], [5, "V"], [4, "IV"],
        [1, "I"]
    ];

    let roman = ""
    for (const [value, symbol] of valueMap) {
        while (num >= value) {
            roman += symbol
            num -= value
        }
    }
    return roman
};

console.log(intToRoman(int1))
console.log(intToRoman(int2))
console.log(intToRoman(int3))


export { }