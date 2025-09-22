function decrypt(code: number[], k: number): number[] {
    if (!k) {
        return new Array<number>(code.length).fill(0)
    }

    const newArray: number[] = []

    for (let i = 0; i < code.length; i++) {
        let newValue = 0

        for (let j = 1; j <= Math.abs(k); j++) {
            if (k > 0) {
                const index = i + j
                newValue += code[index % code.length]
            } else {
                const index = (i - j + code.length) % code.length
                newValue += code[index]
            }
        }

        newArray.push(newValue)
    }

    return newArray
};