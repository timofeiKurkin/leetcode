function maxFreqSum(s: string): number {
    const htVowels: Record<string, number> = {}
    const htConsonants: Record<string, number> = {}

    for (const char of s) {
        if ("aeuio".includes(char)) {
            htVowels[char] = (htVowels[char] || 0) + 1
        } else {
            htConsonants[char] = (htConsonants[char] || 0) + 1
        }
    }

    let maxVowel: number = 0
    for (const v of Object.values(htVowels)) {
        maxVowel = Math.max(maxVowel, v)
    }

    let maxConsonant: number = 0
    for (const v of Object.values(htConsonants)) {
        maxConsonant = Math.max(maxConsonant, v)
    }

    return maxVowel + maxConsonant
};