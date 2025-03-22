function minWindow(s: string, t: string): string {
    if (!s || !t) return ""

    const need = t.split("").reduce((acc, curr) => {
        acc[curr] = (acc[curr] || 0) + 1
        return acc
    }, {} as { [key in string]: number })
    const have: { [key in string]: number } = {}
    const required = Object.keys(need).length
    let formed = 0 // How many chars from need variable is in current piece of string

    let left = 0, right = 0
    let start = 0, minLength = Infinity

    while (right < s.length) {
        const char = s[right]
        have[char] = (have[char] || 0) + 1

        if (char in need && have[char] === need[char])
            formed += 1

        while (left <= right && formed === required) {
            if (right - left + 1 < minLength) {
                minLength = right - left + 1
                start = left
            }

            const leftChar = s[left]
            have[leftChar] -= 1

            if (leftChar in need && have[leftChar] < need[leftChar])
                formed -= 1

            left += 1
        }

        right += 1
    }

    return minLength === Infinity ? "" : s.substring(start, start + minLength)
};


console.log(minWindow("ADOBECODEBANC", "ABC"))
console.log(minWindow("a", "aa"))

export { }

