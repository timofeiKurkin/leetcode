function backspaceCompare(s: string, t: string): boolean {
    return stringHandler(s) === stringHandler(t)
};

function stringHandler(s: string) {
    const stackS: string[] = []

    for (const char of s) {
        if (char === "#") {
            stackS.pop()
        } else {
            stackS.push(char)
        }
    }

    return stackS.join("")
}