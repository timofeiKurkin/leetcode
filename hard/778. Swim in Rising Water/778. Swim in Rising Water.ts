function swimInWater(grid: number[][]): number {
    // const n = grid.length
    // const pathPoints = new Set<number>()
    // const INF = n ** 2

    // const getNextValue = (i: number, j: number) => {
    //     if (i < 0 || j < 0 || i >= n || j >= n || pathPoints.has(grid[i][j])) {
    //         return INF
    //     }

    //     return grid[i][j]
    // }

    // // 0 - top, 1 - right, 2 - bottom, 3 - left
    // const dfs = (i: number, j: number) => {
    //     if (i < 0 || j < 0 || i >= n || j >= n || pathPoints.has(grid[i][j])) {
    //         return
    //     }

    //     pathPoints.add(grid[i][j])

    //     let minimumNext = [INF, i, j] // value, i, j, direction
    //     for (let direction = 0; direction < 4; direction++) {
    //         switch (direction) {
    //             // top
    //             case 0:
    //                 if (getNextValue(i - 1, j) < minimumNext[0]) {
    //                     minimumNext = [grid[i - 1][j], i - 1, j]
    //                 }

    //             // right
    //             case 1:
    //                 if (getNextValue(i, j + 1) < minimumNext[0]) {
    //                     minimumNext = [grid[i][j + 1], i, j + 1]
    //                 }
    //                 break

    //             // bottom
    //             case 2:
    //                 if (getNextValue(i + 1, j) < minimumNext[0]) {
    //                     minimumNext = [grid[i + 1][j], i + 1, j]
    //                 }
    //                 break

    //             // left
    //             case 3:
    //                 if (getNextValue(i, j - 1) < minimumNext[0]) {
    //                     minimumNext = [grid[i][j - 1], i, j - 1]
    //                 }
    //                 break
    //         }
    //     }

    //     if (minimumNext[0] < INF) {
    //         dfs(minimumNext[1], minimumNext[2])
    //     }
    // }

    // for (let i = 0; i < n; i++) {
    //     for (let j = 0; j < n; j++) {
    //         if (!grid[i][j]) {
    //             dfs(i, j)
    //             return pathPoints.size - 1
    //         }
    //     }
    // }

    // return 0

    const n = grid.length

    const possible = (middle: number) => {
        const seen = new Set<string>()

        const dfs = (i: number, j: number) => {
            if ((i === n - 1) && (j === n - 1)) {
                return true
            }

            const key = "" + i + j
            seen.add(key)

            for (const [di, dj] of [[0, 1], [1, 0], [0, -1], [-1, 0]]) {
                const ni = i + di, nj = j + dj
                const key = "" + ni + nj

                if ((ni >= 0 && ni < n) && (nj >= 0 && nj < n) && !seen.has(key)) {
                    if (grid[ni][nj] <= middle && dfs(ni, nj)) {
                        return true
                    }
                }
            }

            return false
        }

        return grid[0][0] <= middle && dfs(0, 0)
    }

    const binarySearch = () => {
        let lowest = grid[0][0], highest = grid.reduce((acc, curr) => Math.max(acc, Math.max(...curr)), 0)

        while (lowest < highest) {
            const middle = Math.floor((lowest + highest) / 2)

            if (possible(middle)) {
                highest = middle
            } else {
                lowest = middle + 1
            }
        }

        return lowest
    }

    return binarySearch()
};