function finalValueAfterOperations(operations: string[]): number {
    let x = 0

    for (const operation of operations) {
        if (operation.startsWith("+") || operation.endsWith("+")) {
            x += 1
        } else {
            x -= 1
        }
    }

    return x
};