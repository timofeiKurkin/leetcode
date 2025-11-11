function calPoints(operations: string[]): number {
    const score: number[] = []

    for (const operation of operations) {
        if (operation === "+" && score.length >= 2) {
            score.push(score[score.length - 1] + score[score.length - 2])
        } else if (operation === "D" && score.length) {
            score.push(score[score.length - 1] * 2)
        } else if (operation === "C") {
            score.pop()
        } else if (!Number.isNaN(parseInt(operation))) {
            score.push(parseInt(operation))
        }
    }

    return score.length ? score.reduce((acc, curr) => acc += curr, 0) : 0
};