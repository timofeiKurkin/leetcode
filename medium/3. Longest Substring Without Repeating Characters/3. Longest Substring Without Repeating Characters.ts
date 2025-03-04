function lengthOfLongestSubstring(s: string): number {
    let left = 0
    let maxLength = 0
    let seen = new Set()

    for (let right = 0; right < s.length; right++) {
        while (seen.has(s[right])) {
            seen.delete(s[left])
            left += 1
        }

        maxLength = Math.max(maxLength, (right - left) + 1)
        seen.add(s[right])
    }

    return maxLength
};