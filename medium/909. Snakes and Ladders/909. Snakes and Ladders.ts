function snakesAndLadders(board: number[][]): number {
    const n = board.length
    board.reverse()

    const getAtPosition = (square: number): [number, number] => {
        const row = Math.floor((square - 1) / n)
        let column = (square - 1) % n

        if (row % 2)
            column = n - 1 - column

        return [row, column]
    }

    const q: number[][] = [[1, 0]] // [square index, steps]
    const visited = new Set()

    while (q.length) {
        let [square, steps] = q.shift()!

        for (let i = 1; i <= 6; i++) {
            let nextSquare = square + i
            const [row, column] = getAtPosition(nextSquare)

            if (board[row][column] !== -1)
                nextSquare = board[row][column]
            if (nextSquare === n ** 2) {
                return steps + 1
            }
            if (!visited.has(nextSquare)) {
                visited.add(nextSquare)
                q.push([nextSquare, steps + 1])
            }
        }
    }

    return -1
};

console.log(snakesAndLadders([[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]))
console.log(snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]))

export { }

