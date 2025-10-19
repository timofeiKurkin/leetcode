/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    const n = s.length

    for (let i = 0; i < Math.round(n / 2); i++) {
        const first = s[i], last = s[n - i - 1]
        s[i] = last
        s[n - i - 1] = first
    }
};
