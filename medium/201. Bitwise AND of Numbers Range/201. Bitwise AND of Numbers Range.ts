function rangeBitwiseAnd(left: number, right: number): number {
    let cnt = 0

    while (left !== right) {
        cnt += 1
        left >>= 1
        right >>= 1
    }

    return left << cnt
};