function minNumberOperations(target: number[]): number {
    let res = 0

    for (let i = 1; i < target.length; i++) {
        if (target[i] < target[i - 1]) {
            res += target[i - 1] - target[i]
        }
    }

    return res + target[target.length - 1]
};