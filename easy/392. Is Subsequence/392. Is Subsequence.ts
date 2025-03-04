function isSubsequence(s: string, t: string): boolean {
    if (!s) return true
    if (!t) return false

    let s_i = 0

    for (const symbol of t) {
        if (s[s_i] == symbol)
            s_i += 1

        if (s_i == s.length)
            return true
    }

    return false
};