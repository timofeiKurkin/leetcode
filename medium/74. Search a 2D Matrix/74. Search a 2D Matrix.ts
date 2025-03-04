function searchMatrix(matrix: number[][], target: number): boolean {
    const binarySearch = <T extends number>(arr: T[], low: T, high: T, target: T): boolean => {

        if (high >= low) {
            const middle = Math.floor((high + low) / 2)
            const num = arr[middle]

            if (num === target)
                return true

            if (num > target)
                return binarySearch(arr, low, middle - 1, target)
            else
                return binarySearch(arr, middle + 1, high, target)
        } else
            return false
    }

    for (let i = 0; i < matrix.length; i++) {
        const res = binarySearch(matrix[i], 0, matrix[i].length - 1, target)

        if (res)
            return true
    }

    return false
};