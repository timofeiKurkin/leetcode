function isValid(s: string): boolean {
    if (s.length % 2 !== 0)
        return false

    const pOpen = ["(", "{", "["]
    const pClose = { ")": "(", "}": "{", "]": "[" }
    const stack: string[] = []

    for (const char of s) {
        if (pOpen.find((p) => p === char)) {
            stack.push(char)
        } else if (char in pClose) {
            if (!stack.length || pClose[char] !== stack.pop())
                return false
        }
    }

    return !stack.length
};