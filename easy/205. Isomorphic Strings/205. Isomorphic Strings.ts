function isIsomorphic(s: string, t: string): boolean {
    const map_s_to_t = new Map()
    const map_t_to_s = new Map()

    for (let i = 0; i <= s.length; i++) {
        if (map_s_to_t.has(s[i])) {
            if (map_s_to_t.get(s[i]) !== t[i]) {
                return false
            }
        }

        if (map_t_to_s.has(t[i])) {
            if (map_t_to_s.get(t[i]) !== s[i]) {
                return false
            }
        }

        map_s_to_t.set(s[i], t[i])
        map_t_to_s.set(t[i], s[i])
    }

    return true
};