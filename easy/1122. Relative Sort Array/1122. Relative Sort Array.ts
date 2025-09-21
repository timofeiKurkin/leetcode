function relativeSortArray(arr1: number[], arr2: number[]): number[] {
    const ht = new Map<number, number>()
    for (const num of arr2) {
        ht.set(num, 0)
    }

    const others: number[] = []

    for (const num of arr1) {
        const prev = ht.get(num)
        if (typeof prev !== "undefined") {
            ht.set(num, prev + 1)
        } else {
            others.push(num)
        }
    }

    others.sort((a, b) => a - b)

    let res: number[] = []

    for (const num of arr2) {
        res = res.concat(repeatItems(num, ht.get(num)!))
    }

    return res.concat(others)
};

function repeatItems<T>(value: T, count: number): T[] {
    const res: T[] = []

    for (let i = 0; i < count; i++) {
        res.push(value)
    }

    return res
}