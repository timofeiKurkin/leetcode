// 13. Roman to Integer
// Римские цифры представляют из себя семь символов: I, V, X, L, C, D и M.
// Symbol       Value
// I            1
// V            5
// X            10
// L            50
// C            100
// D            500
// M            1000
// Для примера 2 - II, а 12 - XII. 27 написано как XXVII, где X + X + V + I + I
// Цифра 4 пишется как IV, а не IIII. Есть шесть случаев, когда используется вычитание:
// - I можно поставить перед V (5) и X (10), чтобы получилось 4 и 9. 
// - X можно поставить перед L (50) и C (100), чтобы получилось 40 и 90. 
// - C можно поставить перед D (500) и M (1000), чтобы получилось 400 и 900.

const s1 = "III" // 3
const s2 = "LVIII" // 58
const s3 = "MCMXCIV" // 1994
const s4 = "XII" // 12
const s5 = "XXVII" // 27

const romanNums: { [key: string]: number } = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

function romanToInt(s: string): number {
    let num = 0

    for (let i = 0; i < s.length; i++) {
        // const joinedRomans = ["IV", "IX", "XL", "XC", "CD", "CM"]
        // const slice = s.slice(i, i + 2)
        // const unitRoman = joinedRomans.indexOf(slice)

        // if (unitRoman !== -1) {
        //     const subtraction = romanNums[joinedRomans[unitRoman][1]] - romanNums[joinedRomans[unitRoman][0]]
        //     num += subtraction
        //     i++
        // }
        
        const currentRom = romanNums[s[i]]
        const nextRom = romanNums[s[i + 1]] || 0
        
        if (currentRom < nextRom) {
            num -= currentRom
        } else {
            num += currentRom
        }
    }

    return num
};

console.log(romanToInt(s1));
console.log(romanToInt(s2));
console.log(romanToInt(s3));
console.log(romanToInt(s4));
console.log(romanToInt(s5));

export { }