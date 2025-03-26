function letterCombinations(digits: string): string[] {
    if (!digits.length)
        return []

    const phoneLetters: { [key in string]: string[] } = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    const res: string[] = []
    const backtrack = (i: number, combination: string) => {
        if (i === digits.length) {
            res.push(combination)
            return
        }

        const digit = digits[i]
        for (const letter of phoneLetters[digit]) {
            backtrack(i + 1, combination + letter)
        }
    }


    backtrack(0, "")
    return res
};


console.log(letterCombinations("23"))
console.log(letterCombinations("22"))

export { }

