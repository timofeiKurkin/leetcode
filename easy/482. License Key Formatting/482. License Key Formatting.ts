function licenseKeyFormatting(s: string, k: number): string {
    const key: string[] = [];
    const joinedKey = s.split("-").join("").toUpperCase();
    const n = joinedKey.length;

    for (let i = n; i >= k; i -= k) {
        key.push(joinedKey.slice(i - k, i));
    }

    if (n % k != 0) key.push(joinedKey.slice(0, n % k));

    return key.toReversed().join("-");
}