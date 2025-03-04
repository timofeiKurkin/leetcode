function mySqrt(x: number): number {
    if (!x)
        return x

    // To solve this problem we should use Heron's Alogrithm
    // Formula: X n+1 = 1/2 * (X n + A / X n)
    // Heron's Alog is iterative and takes an approximate value and returns a new approximate value which is less then the previous one.
    // This can be repeated over and over until the desired accuracy is reached.
    // You can get more info: https://medium.com/@gauravswarankar/heron-algorithm-or-babylonian-method-square-root-14fb599db5d7

    let X_n = Math.round(x / 2)
    let diff = 1
    let accuracy = 0.01

    while (diff > accuracy) {
        const X_n1 = 0.5 * (X_n + x / X_n)
        diff = X_n - X_n1
        X_n = X_n1
    }

    return Math.floor(X_n)
};