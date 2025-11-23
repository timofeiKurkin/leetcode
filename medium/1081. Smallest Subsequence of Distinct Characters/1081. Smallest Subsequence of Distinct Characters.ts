function smallestSubsequence(s: string): string {
    const n = s.length

    const lastOccurrence: Record<string, number> = {}
    for (let i = 0; i < n; i++) {
        lastOccurrence[s[i]] = i
    }

    const stack: string[] = []
    const visited = new Set<string>()

    for (let i = 0; i < n; i++) {
        if (visited.has(s[i])) continue

        while (stack.length && s[i] < stack[stack.length - 1] && i < lastOccurrence[stack[stack.length - 1]]) {
            visited.delete(stack.pop()!)
        }

        visited.add(s[i])
        stack.push(s[i])
    }

    return stack.join("")
};