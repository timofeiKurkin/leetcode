// function pacificAtlantic(heights: number[][]): number[][] {
//     const m = heights.length, n = heights[0].length
//     const pacific = new Set<string>(), atlantic = new Set<string>()

//     function dfs(i: number, j: number, visit: Set<string>, prevHeight: number) {
//         const key = `${i}${j}`
//         if (i < 0 || j < 0 || i >= m || j >= n || heights[i][j] < prevHeight || visit.has(key)) {
//             return
//         }

//         visit.add(key)

//         dfs(i + 1, j, visit, heights[i][j])
//         dfs(i - 1, j, visit, heights[i][j])
//         dfs(i, j + 1, visit, heights[i][j])
//         dfs(i, j - 1, visit, heights[i][j])
//     }

//     for (let j = 0; j < n; j++) {
//         dfs(0, j, pacific, heights[0][j])
//         dfs(m - 1, j, atlantic, heights[m - 1][j])
//     }

//     for (let i = 0; i < m; i++) {
//         dfs(i, 0, pacific, heights[i][0])
//         dfs(i, n - 1, atlantic, heights[i][n - 1])
//     }

//     const res: number[][] = []

//     for (let i = 0; i < m; i++) {
//         for (let j = 0; j < n; j++) {
//             const key = `${i}${j}`
//             if (pacific.has(key) && atlantic.has(key)) {
//                 res.push([i, j])
//             }
//         }
//     }

//     return res
// };

function pacificAtlantic(heights: number[][]): number[][] {
    const m = heights.length, n = heights[0].length;
    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    function dfs(startCells: number[][]) {
        const visited = Array.from({ length: m }, () => Array<boolean>(n).fill(false));
        const stack = [...startCells];
        while (stack.length) {
            const [i, j] = stack.pop()!;
            if (visited[i][j]) continue;
            visited[i][j] = true;
            for (let [dx, dy] of directions) {
                const x = i + dx, y = j + dy;
                if (x >= 0 && x < m && y >= 0 && y < n &&
                    !visited[x][y] && heights[x][y] >= heights[i][j]) {
                    stack.push([x, y]);
                }
            }
        }
        return visited;
    }

    const pacificStarts: number[][] = [];
    for (let j = 0; j < n; j++) pacificStarts.push([0, j]);
    for (let i = 0; i < m; i++) pacificStarts.push([i, 0]);
    const atlanticStarts: number[][] = [];
    for (let j = 0; j < n; j++) atlanticStarts.push([m - 1, j]);
    for (let i = 0; i < m; i++) atlanticStarts.push([i, n - 1]);

    const pacific = dfs(pacificStarts);
    const atlantic = dfs(atlanticStarts);

    const result: number[][] = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (pacific[i][j] && atlantic[i][j]) {
                result.push([i, j]);
            }
        }
    }
    return result;
};
