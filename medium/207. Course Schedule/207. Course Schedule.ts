// Possible solve
// 1. Create graph in "adjacency list" way
// 2. For each course in graph fill an array with pre visited courses
// 3. State will help control the visit status for each course: 0 - NOT visited, 1 - visiting, 2 - completed
// 4. Create DFS function to find a cycle: control visited status in state
// 5. Run DFS function for each course and try to find cycle

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    // Build a graph
    const graph: { [key in number]: number[] } = Object.fromEntries(
        Array.from({ length: numCourses }, (_, i) => [i, []])
    )

    for (const [course, pre] of prerequisites) {
        graph[course].push(pre)
    }

    // State for each course: 0 - NOT visited, 1 - visiting, 2 - completed
    const state = new Array(numCourses).fill(0)

    // DFS function to find cycle in graph, if it exists return true, otherwise - false
    const hasCycle = (course: number): boolean => {
        if (state[course] == 1)
            return true
        else if (state[course] == 2)
            return false

        state[course] = 1

        for (const pre of graph[course]) {
            if (hasCycle(pre))
                return true
        }

        state[course] = 2
        return false

    }

    // Check each course to find a cycle
    for (let course = 0; course < numCourses; course++) {
        const isCycle = hasCycle(course)
        if (isCycle)
            return false
    }

    return true
};


console.log(canFinish(2, [[1, 0]]))
console.log(canFinish(2, [[1, 0], [0, 1]]))

export { }

