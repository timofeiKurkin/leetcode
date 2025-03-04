function hIndex(citations: number[]): number {
    citations.sort((a, b) => a - b).reverse()
    console.log(citations)

    for (let i = 0; i < citations.length - 1; i++) {
        if (citations[i] > i && citations[i + 1] <= i + 1)
            return i + 1
    }

    return citations[0] ? citations.length : 0
};

// console.log(hIndex([3, 0, 6, 1, 5]))
// console.log(hIndex([1, 3, 1]))
// console.log(hIndex([1, 2, 3]))
// console.log(hIndex([11, 15]))
console.log(hIndex([1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3]))