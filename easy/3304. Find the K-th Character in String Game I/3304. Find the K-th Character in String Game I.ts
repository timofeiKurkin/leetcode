function kthCharacter(k: number): string {
    let word = "a"
    while (word.length <= k) {
        const size = word.length
        for (let i = 0; i < size; i++) {
            word += String.fromCharCode("a".charCodeAt(0) + (word.charCodeAt(i) - "a".charCodeAt(0) + 1) % 26)
        }
    }

    return word[k - 1]
};