function exclusiveTime(n: number, logs: string[]): number[] {
    const stack: number[] = []
    let prevTime = 0
    const res = new Array<number>(n).fill(0)

    for (const log of logs) {
        const data = log.split(":")
        const [id, operation, timestamp] = [Number(data[0]), data[1], Number(data[2])]

        if (operation === "start") {
            if (stack.length) {
                res[stack[stack.length - 1]] += timestamp - prevTime
            }

            stack.push(id)
            prevTime = timestamp
        } else {
            res[stack.pop()!] += timestamp - prevTime + 1
            prevTime = timestamp + 1
        }
    }

    return res
};