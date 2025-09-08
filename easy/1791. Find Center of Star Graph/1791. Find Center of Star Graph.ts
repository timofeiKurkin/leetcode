function findCenter(edges: number[][]): number {
    return solution2(edges)
};

function solution1(edges: number[][]): number {
    const graph = new Map<number, number[]>()

    for (const [u, v] of edges) {
        const uEdges = graph.get(u) || []
        uEdges.push(v)
        graph.set(u, uEdges)

        const vEdges = graph.get(v) || []
        vEdges.push(u)
        graph.set(v, vEdges)
    }

    let edge = 0
    let edgeCount = 0

    for (const k of graph.keys()) {
        const node = graph.get(k)!
        if (node.length > edgeCount) {
            edge = k
            edgeCount = node.length
        }
    }

    return edge
}

function solution2(edges: number[][]): number {
    return edges[0][0] === edges[1][0] || edges[0][0] === edges[1][1] ? edges[0][0] : edges[0][1]
}