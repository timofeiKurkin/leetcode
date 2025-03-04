function canConstruct(ransomNote: string, magazine: string): boolean {
    // let ransomNoteIndex = 0
    // let magazineIndex = 0
    // while (magazineIndex < magazine.length) {
    //     magazineIndex += 1
    //     const symbolIndex = magazine.indexOf(ransomNote[ransomNoteIndex])
    //     if (symbolIndex !== -1) {
    //         magazine = magazine.replace(ransomNote[ransomNoteIndex], "")
    //         ransomNoteIndex += 1
    //         magazineIndex -= 1
    //     }
    //     if (ransomNoteIndex === ransomNote.length) {
    //         return true
    //     }
    // }
    // return false

    const chartCount: { [key: string]: number } = {}

    for (const letter of magazine) {
        chartCount[letter] = (chartCount[letter] || 0) + 1
    }

    for (const letter of ransomNote) {
        if (!chartCount[letter] || chartCount[letter] === 0) {
            return false
        }
        chartCount[letter] -= 1
    }

    return true
};


console.log(canConstruct("a", "b"))
console.log(canConstruct("aa", "ab"))
console.log(canConstruct("aa", "aab"))
console.log(canConstruct("aa", "dacafb"))
console.log(canConstruct("aab", "baa"))


export { }