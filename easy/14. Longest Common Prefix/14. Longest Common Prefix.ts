function longestCommonPrefix(strs: string[]): string {
    let prefix = strs[0]

    for (const world of strs) {
        while (!world.startsWith(prefix)) {
            prefix = prefix.slice(0, -1)
            if (!prefix)
                return ""
        }
    }

    return prefix
};


console.log(longestCommonPrefix(["flower", "flow", "flight"]))
console.log(longestCommonPrefix(["dog", "racecar", "car"]))
console.log(longestCommonPrefix(["flower", "flow", "fliwht"]))
console.log(longestCommonPrefix(["reflower", "flow", "flight"]))