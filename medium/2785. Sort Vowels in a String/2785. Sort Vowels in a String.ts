function sortVowels(s: string): string {
    const chars = s.split("")

    const vowelsIndexes: number[] = []
    const vowelItems: string[] = []

    const vowels = new Set<string>(["a", "e", "i", "o", "u"])

    for (let i = 0; i < chars.length; i++) {
        if (vowels.has(chars[i].toLowerCase())) {
            vowelItems.push(chars[i])
            vowelsIndexes.push(i)
        }
    }

    vowelItems.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0))

    for (let i = 0; i < vowelsIndexes.length; i++) {
        chars[vowelsIndexes[i]] = vowelItems[i]
    }

    return chars.join("")
};
