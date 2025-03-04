function hammingWeight(n: number): number {
    let sum = 0
    for (const bit of n.toString(2)) {
        if (bit === "1")
            sum += 1
    }
    return sum
};