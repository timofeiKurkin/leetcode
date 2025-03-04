function wordBreak(s: string, wordDict: string[]): boolean {
    const wordSet = new Set(wordDict)
    const n = s.length
    const dp: boolean[] = Array(n + 1).fill(false)
    dp[0] = true

    for (let i = 1; i < n + 1; i++) {
        for (let j = 0; j < i; j++) {
            if (dp[j] && wordSet.has(s.slice(j, i))) {
                dp[i] = true
                break
            }
        }
    }

    return dp[n]
};


console.log(wordBreak("leetcode", ["leet", "code"]))