function groupAnagrams(strs: string[]): string[][] {
    if (strs.length === 1)
        return [strs]

    const anagrams: { [key in string]: string[] } = {}

    for (const word of strs) {
        const sorted_word = word.split("").sort().join("")

        if (sorted_word in anagrams)
            anagrams[sorted_word].push(word)
        else
            anagrams[sorted_word] = [word]
    }

    return Object.values(anagrams)
};


console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

export { }

