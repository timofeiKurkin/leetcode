function commonChars(words: string[]): string[] {
    let prevFrequency = countFrequency(words[0])

    for (const word of words.slice(1,)) {
        prevFrequency = intersection(prevFrequency, countFrequency(word))
    }

    const res: string[] = []

    for (let i = 0; i < 26; i++) {
        while (prevFrequency[i]) {
            res.push(String.fromCharCode(i + "a".charCodeAt(0)))
            prevFrequency[i]--
        }
    }

    return res
};

function intersection(arr1: number[], arr2: number[]) {
    // arr1.length === arr2.length
    return arr1.map((item, idx) => Math.min(item, arr2[idx]))
}

function countFrequency(word: string) {
    const frequency = new Array<number>(26).fill(0)

    for (const letter of word) {
        frequency[letter.charCodeAt(0) - "a".charCodeAt(0)]++
    }

    return frequency
}