function validPalindrome(s: string): boolean {
    // for (let i = 0; i < s.length; i++) {
    //     const current = s.slice(0, i) + s.slice(i + 1,)
    //     let n = Math.floor(current.length / 2)

    //     let f = n - 1, l = n

    //     if (current.length % 2 != 0) {
    //         l += 1
    //     }

    //     let status = true

    //     while (f >= 0) {
    //         if (status) {
    //             if (current[f] != current[l]) {
    //                 status = false
    //             }

    //             f -= 1
    //             l += 1
    //         } else
    //             break
    //     }

    //     if (status)
    //         return status
    // }

    // return false

    const isPalindrome = (start: number, end: number): boolean => {
        while (start < end) {
            if (s[start] != s[end]) return false
            start++
            end--
        }
        return true
    }

    let left = 0, right = s.length - 1

    while (left < right) {
        if (s[left] != s[right]) {
            return isPalindrome(left + 1, right) || isPalindrome(left, right - 1)
        }
        left++
        right--
    }

    return true
};


console.log(validPalindrome("aba"))
console.log(validPalindrome("abca"))
console.log(validPalindrome("abc"))

console.log(validPalindrome("acbca"))


export { }