function generate(numRows: number): number[][] {
    const triangle = Array.from({ length: numRows }, (_, i) => new Array<number>(i + 1).fill(1))

    for (let i = 2; i < numRows; i++) {
        for (let j = 1; j < i; j++) {
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        }
    }

    return triangle
};