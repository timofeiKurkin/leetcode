function canVisitAllRooms(rooms: number[][]): boolean {
    const visited = new Set()
    const n = rooms.length

    const dfs = (idx: number) => {
        if (visited.has(idx)) return
        visited.add(idx)
        for (const room of rooms[idx]) {
            dfs(room)
        }
    }

    dfs(0)

    return n == visited.size
};