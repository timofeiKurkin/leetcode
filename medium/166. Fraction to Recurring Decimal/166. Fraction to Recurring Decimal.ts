function fractionToDecimal(numerator: number, denominator: number): string {
    if (numerator === 0) {
        return "0"
    }

    const fraction: string[] = []

    if ((numerator < 0) !== (denominator < 0)) {
        fraction.push("-")
    }

    const dividend = Math.abs(numerator)
    const divisor = Math.abs(denominator)

    fraction.push(String(Math.floor(dividend / divisor)))
    let remainder = dividend % divisor

    if (remainder === 0) {
        return fraction.join("")
    }

    fraction.push(".")
    const mapDict: { [key: number]: number } = {}

    while (remainder) {
        if (remainder in mapDict) {
            fraction.splice(mapDict[remainder], 0, "(")
            fraction.push(")")
            break
        }

        mapDict[remainder] = fraction.length
        remainder *= 10
        fraction.push(String(Math.floor(remainder / divisor)))
        remainder %= divisor
    }

    return fraction.join("")
};