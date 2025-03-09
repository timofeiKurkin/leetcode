function substrFromCenter(s: string, start: number, end: number): string {
    while (start >= 0 && end < s.length && s[start] === s[end]) {
        start -= 1
        end += 1
    }
    return s.slice(start + 1, end)
}

function longestPalindrome(s: string): string {
    if (s.length === 1)
        return s

    let maxSubstr = ""

    for (let i = 0; i < s.length; i++) {
        const evenSubstr = substrFromCenter(s, i, i)
        const oddSubstr = substrFromCenter(s, i, i + 1)

        maxSubstr = (evenSubstr.length > maxSubstr.length && evenSubstr.length > oddSubstr.length) ? evenSubstr : (oddSubstr.length > maxSubstr.length) ? oddSubstr : maxSubstr
    }

    return maxSubstr
};