function minimumOneBitOperations(n: number): number {
    let operations = 0

    while (n) {
        operations ^= n
        n >>= 1
    }

    return operations
};