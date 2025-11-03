function minCost(colors: string, neededTime: number[]): number {
    let res = 0, i = 0

    while (i < colors.length) {
        if (colors[i] === colors[i + 1]) {
            let end = i + 1, totalTime = neededTime[i], maxTime = neededTime[i]

            while (end < colors.length && colors[i] === colors[end]) {
                maxTime = Math.max(maxTime, neededTime[end])
                totalTime += neededTime[end]
                end += 1
            }

            res += totalTime - maxTime
            i = end
        } else {
            i += 1
        }
    }

    return res
};