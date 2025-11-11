function makeGood(s: string): string {
    const stack: string[] = []

    for (let char of s) {
        if (stack.length) {
            const last = stack[stack.length - 1]

            if (char !== last && (char.toLowerCase() === last || char === last.toLowerCase())) {
                stack.pop()
            } else {
                stack.push(char)
            }
        } else {
            stack.push(char)
        }
    }

    return stack.join("")
};
