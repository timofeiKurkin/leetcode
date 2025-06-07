type QueueType = [number, number][]

function orangesRotting(grid: number[][]): number {
    const n = grid.length, m = grid[0].length
    let zeroes = 0, oranges = 0
    const queue: QueueType = []

    const validPosition = (i: number, j: number): boolean => {
        return i >= 0 && j >= 0 && i < n && j < m && grid[i][j] === 1
    }

    const checkDirections = (i: number, j: number, queue: QueueType) => {
        if (validPosition(i + 1, j)) {
            grid[i + 1][j] = -1
            queue.push([i + 1, j])
        }
        if (validPosition(i - 1, j)) {
            grid[i - 1][j] = -1
            queue.push([i - 1, j])
        }
        if (validPosition(i, j + 1)) {
            grid[i][j + 1] = -1
            queue.push([i, j + 1])
        }
        if (validPosition(i, j - 1)) {
            grid[i][j - 1] = -1
            queue.push([i, j - 1])
        }
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (grid[i][j] === 0) {
                zeroes += 1
                continue
            }

            if (grid[i][j] === 2) {
                oranges += 1
                checkDirections(i, j, queue)
            }
        }
    }

    let minutes = 0

    while (queue.length) {
        let localOranges = 0

        for (let d = 0; d < queue.length; d++) {
            const [i, j] = queue.shift()!

            if (Math.abs(grid[i][j]) !== 1) continue

            grid[i][j] = 2
            localOranges += 1
            checkDirections(i, j, queue)
        }


        if (localOranges) {
            minutes += 1
            oranges += localOranges
        }
    }

    if (oranges + zeroes != m * n) return -1
    return minutes
};