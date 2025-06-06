function findCircleNum(provinces: number[][]): number {
    const visited = new Set()
    const n = provinces.length
    let res = 0

    const dfs = (city: number) => {
        if (visited.has(city)) return
        visited.add(city)
        for (let conn = 0; conn < n; conn) {
            if (provinces[city][conn] == 1)
                dfs(conn)
        }
    }

    for (let city = 0; city < n; city++) {
        if (visited.has(city)) continue
        dfs(city)
        res += 1
    }

    return res
};