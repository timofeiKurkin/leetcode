const mapsAreEqual = <K, T>(firstMap: Map<K, T>, secondMap: Map<K, T>): boolean => {
    for (const [key, value] of firstMap) {
        if (secondMap.get(key) !== value) return false
    }
    return true
}

function findAnagrams(s: string, p: string): number[] {
    // const pp = p.split("").sort().join("")
    // const n = p.length
    // const res: number[] = []
    // for (let i = 0; i <= s.length - n; i++) {
    //     if (s.slice(i, i + n).split("").sort().join("") === pp)
    //         res.push(i)
    // }
    // return res

    if (s.length < p.length) return []

    const pMap = new Map<string, number>()
    const examineMap = new Map<string, number>()
    for (let i = 0; i < p.length; i++) {
        pMap.set(p[i], (pMap.get(p[i]) || 0) + 1)
        examineMap.set(s[i], (examineMap.get(s[i]) || 0) + 1)
    }

    const res: number[] = []
    let end = p.length

    while (end < s.length) {
        if (mapsAreEqual(pMap, examineMap))
            res.push(end - p.length)

        const endChar = s.charAt(end)
        examineMap.set(endChar, (examineMap.get(endChar) || 0) + 1)

        const currentChar = s.charAt(end - p.length)
        const currExamine = examineMap.get(currentChar)
        if (currExamine) {
            if (currExamine === 1) examineMap.delete(currentChar)
            else examineMap.set(currentChar, currExamine - 1)
        }

        end += 1
    }

    if (mapsAreEqual(pMap, examineMap))
        res.push(end - p.length)

    return res

};