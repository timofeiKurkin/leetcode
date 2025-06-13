function isPalindrome(s: string) {
    return s === s.split("").reverse().join("")
}

function partition(s: string): string[][] {
    const n = s.length
    const res: string[][] = []

    const backtrack = (index: number, path: string[]) => {
        if (index === n) {
            res.push(path)
            return
        }

        for (let i = index + 1; i <= n; i++) {
            if (isPalindrome(s.slice(index, i)))
                backtrack(i, [...path, s.slice(index, i)])
        }
    }

    backtrack(0, [])

    return res
};


export { }

