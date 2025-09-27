function largestTriangleArea(points: number[][]): number {
    const n = points.length
    let res = 0

    for (let i = 0; i < n; i++) {
        const [x1, y1] = points[i]

        for (let j = i + 1; j < n; j++) {
            const [x2, y2] = points[j]

            for (let k = j + 1; k < n; k++) {
                const [x3, y3] = points[k]
                const area = 1 / 2 * Math.abs(
                    x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
                )
                res = Math.max(res, area)
            }
        }
    }

    return res
};