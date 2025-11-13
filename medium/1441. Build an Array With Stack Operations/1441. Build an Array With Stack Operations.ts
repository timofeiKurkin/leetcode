function buildArray(target: number[], n: number): string[] {
    const targetSet = new Set(target)
    const maxValue = Math.max(...target)
    const operations: string[] = []
    for (let i = 1; i <= maxValue; i++) {
        operations.push("Push")
        if (!targetSet.has(i)) {
            operations.push("Pop")
        }
    }

    return operations
};