function addBinary(a: string, b: string): string {
    const maxLen = Math.max(a.length, b.length)
    a = a.padStart(maxLen, '0');
    b = b.padStart(maxLen, '0');
    const result: number[] = []

    let carry = 0

    for (let i = maxLen - 1; i >= 0; i--) {
        const b1 = Number(a[i])
        const b2 = Number(b[i])

        const total = b1 + b2 + carry
        result.push(total % 2)
        carry = Math.floor(total / 2)
    }

    if (carry)
        result.push(1)


    result.reverse()
    return result.join("")
};

console.log(addBinary("11", "1"))
console.log(addBinary("1010", "1011"))
console.log(addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101",
    "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"))

// console.log("0".repeat(2))
// console.log("0".repeat(0))