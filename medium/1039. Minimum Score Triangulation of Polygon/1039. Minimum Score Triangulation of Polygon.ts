function minScoreTriangulation(values: number[]): number {
    const n = values.length
    if (n === 3) {
        return values[0] * values[1] * values[2]
    }

    const dp = Array.from({ length: n - 1 }, () => new Array<number>(n).fill(0))

    for (let v = 2; v < n; v++) {
        for (let i = 0; i < n - v; i++) {
            const j = i + v
            let minTriangulation = Infinity
            const sides = values[i] * values[j]

            for (let k = i + 1; k < j; k++) {
                minTriangulation = Math.min(minTriangulation, sides * values[k] + dp[i][k] + dp[k][j])
            }

            dp[i][j] = minTriangulation
        }
    }

    return dp[0][n - 1]
};