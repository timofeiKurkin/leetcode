function findLucky(arr: number[]): number {
    const cnt = new Map<number, number>()

    for (const item of arr) {
        cnt.set(item, cnt.get(item) || 0)
    }

    let res = -1

    for (const item of cnt.keys()) {
        if (item === cnt.get(item)) res = Math.max(res, item)
    }

    return res
};