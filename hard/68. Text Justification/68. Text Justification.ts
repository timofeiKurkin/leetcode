function fullJustify(words: string[], maxWidth: number): string[] {
    const result: string[] = []
    let currLine: string[] = []
    let currLength = 0

    for (const word of words) {
        if (currLength + word.length + currLine.length > maxWidth) {
            for (let i = 0; i < maxWidth - currLength; i++) {
                currLine[i % (currLine.length - 1 || 1)] += " "
            }
            result.push(currLine.join(""))
            currLine = [], currLength = 0
        }

        currLine.push(word)
        currLength += word.length
    }

    const lastLine = currLine.join(" ")
    result.push(lastLine + " ".repeat((maxWidth - lastLine.length)))

    return result
};