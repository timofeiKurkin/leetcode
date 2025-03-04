/**
 * Definition for _Node.
 */

class _Node {
    val: number
    neighbors: _Node[]

    constructor(val?: number, neighbors?: _Node[]) {
        this.val = (val === undefined ? 0 : val)
        this.neighbors = (neighbors === undefined ? [] : neighbors)
    }
}


function cloneGraph(node: _Node | null): _Node | null {
    if (!node)
        return null

    const visited = {}

    const clone = (curr: _Node): _Node => {
        if (curr.val in visited)
            return visited[curr.val]

        const copy = new _Node(curr.val)
        visited[curr.val] = copy

        for (const neighbor of curr.neighbors) {
            copy.neighbors.push(clone(neighbor))
        }

        return copy
    }

    return clone(node)
};