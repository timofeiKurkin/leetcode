function repeatedStringMatch(a: string, b: string): number {
    const n = a.length, m = b.length
    let times = Math.ceil(m / n)
    const substring = a.repeat(times)

    if (substring.includes(b)) return times
    if ((substring + a).includes(b)) return times + 1
    return - 1
};