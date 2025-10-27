function numberOfBeams(bank: string[]): number {
    const lasersOnLevels: number[] = []
    for (const level of bank) {
        const ones = countOnes(level)
        if (ones) {
            lasersOnLevels.push(ones)
        }
    }

    let res = 0
    for (let i = 0; i < lasersOnLevels.length - 1; i++) {
        res += lasersOnLevels[i] * lasersOnLevels[i + 1]
    }

    return res
};

function countOnes(row: string): number {
    return row.split("").reduce((acc, curr) => acc += curr === "1" ? 1 : 0, 0)
}