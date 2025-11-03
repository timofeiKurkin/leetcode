function countUnguarded(m: number, n: number, guards: number[][], walls: number[][]): number {
    return solution2(m, n, guards, walls)
};

function solution1(m: number, n: number, guards: number[][], walls: number[][]): number {
    // It doesn't work. The logic is to subtract guards, walls and protected cells
    const wallsSet = new Set<string>(), guardsSet = new Set<string>(), cellsSet = new Set<string>()

    for (const wall of walls) {
        wallsSet.add(wall.join(""))
    }

    for (const guard of guards) {
        guardsSet.add(guard.join(""))
    }

    function dfs(i: number, j: number, direction: number): void {
        const key = "" + i + j
        if (i < 0 || j < 0 || i >= m || j >= n || wallsSet.has(key) || guardsSet.has(key)) {
            return
        }

        cellsSet.add(key)
        // 0 - top, 1 - right, 2 - bottom, 3 - left
        if (direction === 0) {
            return dfs(i - 1, j, direction)
        } else if (direction === 1) {
            return dfs(i, j + 1, direction)
        } else if (direction === 2) {
            return dfs(i + 1, j, direction)
        } else {
            return dfs(i, j - 1, direction)
        }
    }

    for (const guard of guards) {
        const [i, j] = guard
        dfs(i - 1, j, 0)
        dfs(i, j + 1, 1)
        dfs(i + 1, j, 2)
        dfs(i, j - 1, 3)
    }

    return m * n - cellsSet.size - wallsSet.size - guardsSet.size
}

function solution2(m: number, n: number, guards: number[][], walls: number[][]): number {
    // 0 - empty, 1 - guard || wall, 2 - protected cell
    // const matrix = new Array()
    const matrix = Array.from<number[], number[]>({ length: m }, () => new Array(n).fill(0))

    for (const wall of walls) {
        const [i, j] = wall
        matrix[i][j] = 1
    }

    const directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for (const guard of guards) {
        const [i, j] = guard
        matrix[i][j] = 1
    }

    for (const guard of guards) {
        const [i, j] = guard

        for (const [di, dj] of directions) {
            let ni = i + di
            let nj = j + dj

            while (ni >= 0 && nj >= 0 && ni < m && nj < n && matrix[ni][nj] !== 1) {
                matrix[ni][nj] = 2
                ni += di
                nj += dj
            }
        }
    }

    let res = 0
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] === 0) {
                res += 1
            }
        }
    }

    return res
}