function minimumAbsDifference(arr: number[]): number[][] {
    arr.sort((a, b) => a - b)

    let minDifference = Infinity
    let res: number[][] = []

    for (let i = 0; i < arr.length - 1; i++) {
        const localMin = Math.abs(arr[i] - arr[i + 1])

        if (localMin < minDifference) {
            minDifference = localMin
            res = [[arr[i], arr[i + 1]]]
        } else if (localMin === minDifference) {
            res.push([arr[i], arr[i + 1]])
        }
    }

    return res
};