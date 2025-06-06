function minReorder(n: number, connections: number[][]): number {
    const visited = new Set([0])
    let res = 0

    while (visited.size < n) {
        const toCheck = []

        for (const conn of connections) {
            if (visited.has(conn[1])) {
                visited.add(conn[0])
            } else if (visited.has(conn[0])) {
                visited.add(conn[1])
                res += 1
            } else {
                toCheck.push(conn)
            }
        }

        connections = toCheck.toReversed()
    }

    return res
};