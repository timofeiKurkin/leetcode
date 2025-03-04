function isPalindrome(s: string): boolean {
    // const fs = s.toLowerCase().split("").filter((item) => /^[A-Za-z0-9]*$/.test(item)).join("")
    let fs = ""

    for (const item of s) {
        if (/^[A-Za-z0-9]*$/.test(item))
            fs += item.toLowerCase()
    }

    const n = Math.floor(fs.length / 2)
    let f = n - 1, l = n

    if (fs.length % 2 != 0) {
        l += 1
    }

    while (f >= 0) {
        if (fs[f] != fs[l])
            return false
        f -= 1
        l += 1
    }

    return true
};


console.log(isPalindrome("A man, a plan, a canal: Panama"))
console.log(isPalindrome("race a car"))
console.log(isPalindrome(" "))
console.log(isPalindrome("ab"))
console.log(isPalindrome('Marge, let\'s "[went]." I await {news} telegram.'))
console.log(isPalindrome("0P"))

export { }