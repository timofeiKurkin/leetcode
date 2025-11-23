function timeRequiredToBuy(tickets: number[], k: number): number {
    let steps = 0
    while (k !== -1) {
        const tick = tickets.shift()!

        if (tick == 1) {
            if (!k) {
                k = -1
            } else {
                k -= 1
            }
        } else {
            tickets.push(tick - 1)

            if (!k) {
                k = tickets.length - 1
            } else {
                k -= 1
            }
        }

        steps += 1
    }

    return steps
};