function findWordsContaining(words: string[], x: string): number[] {
    const res: number[] = []

    words.forEach((w, i) => {
        if (w.indexOf(x) != -1) {
            res.push(i)
        }
    })

    return res
};