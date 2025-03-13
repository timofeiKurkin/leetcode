function maximalSquare(matrix: string[][]): number {
    const m = matrix.length
    const n = matrix[0].length
    const dp = Array.from({ length: m }, () => Array(n).fill(0))

    let maxSize = 0

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] == "1") {
                if (!i || !j)
                    dp[i][j] = 1
                else
                    dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxSize = Math.max(dp[i][j], maxSize)
            }
        }
    }

    return maxSize * maxSize
};