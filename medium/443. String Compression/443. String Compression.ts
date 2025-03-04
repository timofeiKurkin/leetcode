const chars1 = ["a", "a", "b", "b", "c", "c", "c"]
const chars2 = ["a"]
const chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
const chars4 = ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b", "a", "b", "a"]

function compress(chars: string[]): number {
    if (chars.length === 1) return chars.length

    // let uniqueItemIndex = 0
    // let repeat = 1
    // const s: (string | number)[] = []

    // for (let i = 0; i < chars.length; i++) {

    //     if (chars[i] === chars[i + 1]) {
    //         repeat += 1

    //         if (repeat >= 10) {
    //             if (repeat === 10) {
    //                 s.splice(uniqueItemIndex + 1, 1, ...String(repeat).split(""))
    //             } else {
    //                 s.splice(uniqueItemIndex + 2, 1, String(repeat).split("")[1])
    //             }
    //         } else
    //             s[uniqueItemIndex + 1] = String(repeat)
    //     } else {
    //         s[uniqueItemIndex] = chars[i]
    //         if (Number(s[uniqueItemIndex + 1]))
    //             uniqueItemIndex += 2
    //         else
    //             uniqueItemIndex += 1
    //         repeat = 1
    //     }
    // }

    let uniqueIndex = 0
    let index = 0

    while (index < chars.length) {
        const currentChar = chars[index]
        let count = 0

        while (index < chars.length && chars[index] === currentChar) {
            index++
            count++
        }

        chars[uniqueIndex] = currentChar
        uniqueIndex++

        if (count > 1) {
            for (const digit of String(count)) {
                chars[uniqueIndex] = digit
                uniqueIndex++
            }
        }
    }

    return chars.length
};

console.log(compress(chars1));
console.log(compress(chars2));
console.log(compress(chars3));
console.log(compress(chars4));

export { }