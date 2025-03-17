function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    const graph: { [key in string]: { [key in string]: number } } = {}
    // Build graph
    for (let i = 0; i < equations.length; i++) {
        const [A, B] = equations[i]
        const value = values[i]

        graph[A] = { ...graph[A], [B]: value }
        graph[B] = { ...graph[B], [A]: 1 / value }
    }

    // Search function for calculating
    const dfs = (C: string, D: string, visited: Set<string>): number => {
        // Check if there is no variable in the whole graph
        if (!(C in graph) || !(D in graph)) {
            return -1.0
        }

        // If one variable is the same to another: A / A = 1
        if (C === D) {
            return 1.0
        }

        visited.add(C)

        for (const neighbor in graph[C]) {
            if (!visited.has(neighbor)) {
                const value = graph[C][neighbor]
                const result = dfs(neighbor, D, visited)
                if (result !== -1.0) {
                    return result * value
                }
            }
        }

        return -1.0
    }

    // Calculate queries
    const result: number[] = []

    for (const [C, D] of queries) {
        result.push(dfs(C, D, new Set()))
    }

    return result
};

console.log(calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))

export { }

