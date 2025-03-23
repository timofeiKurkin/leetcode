function findOrder(numCourses: number, prerequisites: number[][]): number[] {
    const graph: { [key in number]: number[] } = Object.fromEntries(
        Array.from({ length: numCourses }, (_, i) => [i, []])
    )

    for (const [course, pre] of prerequisites) {
        graph[course].push(pre)
    }

    const state = new Array(numCourses).fill(0)
    const visited = new Set()

    const hasCycle = (course: number): [boolean, number] => {
        if (!graph[course].length)
            return [true, state[course]]
        if (visited.has(course))
            return [false, Infinity]

        visited.add(course)
        for (const pre of graph[course]) {
            const [doable, order] = hasCycle(pre)
            if (!doable) return [false, Infinity]
            state[course] = Math.max(state[course], 1 + order)
        }

        graph[course] = []
        return [true, state[course]]
    }

    for (let course = 0; course < numCourses; course++) {
        const [doable, _] = hasCycle(course)
        if (!doable)
            return []
    }

    return Array.from({ length: numCourses }, (_, i) => state[i]) // .sort((a, b) => state[a] - state[b])
};

export { }

