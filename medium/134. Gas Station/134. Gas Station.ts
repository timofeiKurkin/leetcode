function canCompleteCircuit(gas: number[], cost: number[]): number {
    const l = gas.length
    let tank = 0, curr_tank = 0
    let start = 0

    for (let i = 0; i < l; i++) {
        tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]

        if (curr_tank < 0) {
            curr_tank = 0
            start = i + 1
        }
    }

    return tank >= 0 ? start : -1
};