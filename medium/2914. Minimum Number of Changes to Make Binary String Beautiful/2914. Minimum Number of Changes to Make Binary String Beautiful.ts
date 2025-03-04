function minChanges(s: string): number {
    if (!s.includes("0") || !s.includes("1")) return 0
    let res = 0

    for (let i = 0; i < s.length; i += 2) {
        if (s[i] !== s[i + 1]) {
            res += 1
        }
    }

    return res
};


console.log("1001: ", minChanges("1001"))
console.log("10: ", minChanges("10"))
console.log("0000: ", minChanges("0000"))
console.log("110100: ", minChanges("110100"))
console.log("110101: ", minChanges("110101"))
console.log("100110: ", minChanges("100110"))