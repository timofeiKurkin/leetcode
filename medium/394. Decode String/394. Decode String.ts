function decodeString(s: string): string {
    if (s.length == 1) return s

    const run = (index: number): [string, number] => {
        let res = ""

        while (index < s.length) {
            if (!isNaN(parseFloat(s[index]))) {
                let k = 0
                while (!isNaN(parseFloat(s[index]))) {
                    k = k * 10 + parseFloat(s[index])
                    index += 1
                }

                index += 1
                const [decodedString, newIndex] = run(index)
                index = newIndex
                res += decodedString.repeat(k)
            } else if (s[index] === "]") {
                return [res, index + 1]
            } else {
                res += s[index]
                index += 1
            }
        }

        return [res, index]
    }

    const [res, _] = run(0)
    return res
};