function repeatedSubstringPattern(s: string): boolean {
    const n = s.length;

    if (n === 1) return false

    for (let i = 0; i < n / 2; i++) {
        const substring = s.slice(0, i + 1);
        if (!(n % substring.length)) {
            if (substring.repeat(n / substring.length) === s) return true;
        }
    }

    return false;
}