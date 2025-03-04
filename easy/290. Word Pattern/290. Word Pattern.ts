function wordPattern(pattern: string, s: string): boolean {
    const sArr = s.split(" ")

    if (sArr.length !== pattern.length) {
        return false
    }

    const patternToWord = new Map()
    const wordToPattern = new Map()

    for (let i = 0; i < sArr.length; i++) {
        if ((patternToWord.has(pattern[i]) && patternToWord.get(pattern[i]) !== sArr[i]) || (wordToPattern.has(sArr[i]) && patternToWord.get(sArr[i]) !== pattern[i]))
            return false

        patternToWord.set(pattern[i], sArr[i])
        wordToPattern.set(sArr[i], pattern[i])
    }

    return true
};