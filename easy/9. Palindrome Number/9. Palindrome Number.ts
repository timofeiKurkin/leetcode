function isPalindrome(x: number): boolean {
    if (x < 0) return false
    const str = String(x)

    if (str.length === 1) return true

    let first = 0, second = str.length - 1, end = Math.floor(str.length / 2)

    if (str.length % 2 !== 0) {
        end += 1
    }

    while (first <= end) {
        if (str[first] !== str[second]) {
            return false
        }
        first += 1
        second -= 1
    }

    return true
};


console.log(isPalindrome(123))
console.log(isPalindrome(121))
console.log(isPalindrome(-121))
console.log(isPalindrome(10))
console.log(isPalindrome(1001))
