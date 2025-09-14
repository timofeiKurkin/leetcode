function spellchecker(wordlist: string[], queries: string[]): string[] {
    const ht = new Map<string, string[]>()

    for (const word of wordlist) {
        const wordKey = normalizeVowels(word)

        ht.set(wordKey, [...(ht.get(wordKey) || []), word])
    }

    const res: string[] = []

    for (const query of queries) {
        const words = ht.get(normalizeVowels(query))
        if (words) {
            res.push(findMaximumMatch(words, query))
        } else {
            res.push("")
        }
    }

    return res
};

function normalizeVowels(word: string): string {
    return word.toLowerCase().replace(/[aeiou]/gi, "*")
}

function findMaximumMatch(words: string[], word: string): string {
    return (
        words.find((item) => word === item) ||
        words.find((item) => word.toLocaleLowerCase() === item.toLocaleLowerCase()) ||
        words[0]
    )
}