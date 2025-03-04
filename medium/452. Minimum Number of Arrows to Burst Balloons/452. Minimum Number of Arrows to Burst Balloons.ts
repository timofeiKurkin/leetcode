function findMinArrowShots(points: number[][]): number {
    if (!points.length)
        return 0

    const sortedPoints = points.sort((a, b) => a[1] - b[1])
    let arrow = 1
    let end = sortedPoints[0][1]

    for (let i = 1; i < sortedPoints.length; i++) {
        if (end < sortedPoints[i][0]) {
            arrow += 1
            end = sortedPoints[i][1]
        }
    }

    return arrow
};