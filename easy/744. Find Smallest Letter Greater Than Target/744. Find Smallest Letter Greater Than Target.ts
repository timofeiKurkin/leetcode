function nextGreatestLetter(letters: string[], target: string): string {
    let best = letters[0]

    for (let i = 0; i <= letters.length; i++) {
        const current = letters[i]
        if (current !== target && current > target) {
            return current
        }
    }

    return best
};