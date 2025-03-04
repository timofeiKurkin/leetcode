function rotate(matrix: number[][]): void {
    const n = matrix[0].length
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            const first = matrix[i][j]
            const second = matrix[j][i]

            matrix[i][j] = second
            matrix[j][i] = first
        }
    }

    for (let i = 0; i < n; i++) {
        matrix[i].reverse()
    }
};

const matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)