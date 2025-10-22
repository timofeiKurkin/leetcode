function flipAndInvertImage(image: number[][]): number[][] {
    for (const row of image) {
        reverse(row)
        invertImage(row)
    }

    return image
};

function reverse<T>(s: T[]): void {
    const n = s.length

    for (let i = 0; i < Math.round(n / 2); i++) {
        const first = s[i], last = s[n - i - 1]
        s[i] = last
        s[n - i - 1] = first
    }
};

function invertImage(s: number[]): void {
    for (let i = 0; i < s.length; i++) {
        s[i] = Number(!s[i])
    }
}