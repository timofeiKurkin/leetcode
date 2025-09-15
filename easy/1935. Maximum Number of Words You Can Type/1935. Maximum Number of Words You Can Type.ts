function canBeTypedWords(text: string, brokenLetters: string): number {
    let res = 0
    let isValid = true

    for (const char of text + " ") {
        if (brokenLetters.includes(char)) {
            isValid = false
        } else if (char === " ") {
            if (isValid) {
                res += 1
            } else {
                isValid = true
            }
        }
    }

    return res
};