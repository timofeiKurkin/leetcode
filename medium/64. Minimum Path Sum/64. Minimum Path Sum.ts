function minPathSum(grid: number[][]): number {
    const n = grid.length
    const m = grid[0].length
    const template: number[][] = [] // Array.from({ length: n }, () => Array(m).fill(0))
    for (let i = 0; i < n; i++) {
        template.push(new Array(m).fill(0))
    }
    template[0][0] = grid[0][0]

    for (let i = 1; i < n; i++) {
        template[i][0] = grid[i][0] + template[i - 1][0]
    }

    for (let j = 1; j < m; j++) {
        template[0][j] = grid[0][j] + template[0][j - 1]
    }

    for (let i = 1; i < n; i++) {
        for (let j = 1; j < m; j++) {
            template[j][0] = Math.min(grid[i][j] + template[i - 1][j], grid[i][j] + template[i][j - 1])
        }
    }

    return template[n][m]
};

export { }
