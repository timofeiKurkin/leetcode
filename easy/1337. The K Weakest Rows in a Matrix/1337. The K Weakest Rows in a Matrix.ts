function kWeakestRows(mat: number[][], k: number): number[] {
    const rows = [] // [index, soldiers]
    const n = mat.length, m = mat[0].length

    for (let i = 0; i < n; i++) {
        rows.push([i, binSearch(mat[i])])
    }

    return rows.sort((a, b) => a[1] - b[1]).slice(0, k).map((item) => item[0])
};

function binSearch(nums: number[]) {
    let start = 0, end = nums.length

    while (start < end) {
        const middle = Math.floor((start + end) / 2)

        if (nums[middle] === 1) {
            start = middle + 1
        } else {
            end = middle
        }
    }

    return end
}
