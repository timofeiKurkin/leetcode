function isAnagram(s: string, t: string): boolean {
    // if (s.length !== t.length)
    //     return false

    // const sortedS = s.split("").sort()
    // const sortedT = t.split("").sort()

    // for (let i = 0; i < sortedS.length; i++) {
    //     if (sortedS[i] !== sortedT[i])
    //         return false
    // }

    // return true

    const counter: Record<string, number> = {}

    for (const letter of s) {
        counter[letter] = counter[letter] ?? 0 + 1
    }

    for (const letter of t) {
        counter[letter] = counter[letter] ?? 0 - 1
    }

    for (const count of Object.values(counter)) {
        if (count !== 0) return false
    }

    return true
};

console.log(isAnagram("anagram", "nagaram"))
console.log(isAnagram("rat", "car"))