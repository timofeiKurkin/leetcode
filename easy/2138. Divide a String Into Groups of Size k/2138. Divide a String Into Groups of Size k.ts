function divideString(s: string, k: number, fill: string): string[] {
    const res: string[] = []
    for (let i = 0; i < s.length; i += k) {
        res.push(s.slice(i, i + k))
    }

    const lastSize = res[res.length - 1].length
    if (lastSize < k) {
        res[res.length - 1] += fill.repeat(k - lastSize)
    }

    return res
};