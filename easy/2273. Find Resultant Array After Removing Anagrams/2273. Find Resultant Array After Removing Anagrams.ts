function isAnagram(str1: string, str2: string): boolean {
    if (str1.length !== str2.length) {
        return false
    }

    str1 = str1.split('').sort().join('')
    str2 = str2.split('').sort().join('')

    return str1 === str2
}

function removeAnagrams(words: string[]): string[] {
    const res: string[] = [words[0]]

    for (let i = 1; i < words.length; i++) {
        if (!isAnagram(words[i - 1], words[i])) {
            res.push(words[i])
        }
    }

    return res
};