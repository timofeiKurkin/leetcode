function getBaseLog(x: number, y: number): number {
    return Math.log(y) / Math.log(x);
}

function isPowerOfFour(n: number): boolean {
    const base = getBaseLog(4, n)
    return base % 1 === 0
};