function isCircularSentence(sentence: string): boolean {
    const senArr = sentence.split(" ")

    if (senArr.length === 1) {
        const curr = senArr[0]
        return curr[0] === curr.slice(-1)
    }

    for (let i = 0; i < senArr.length - 1; i++) {
        const curr = senArr[i]
        const next = senArr[i + 1]
        if (curr.slice(-1) !== next[0]) {
            return false
        }
    }

    const last = senArr.slice(-1)[0]
    return senArr[0][0] === last.slice(-1)
};

console.log(isCircularSentence("leetcode exercises sound delightful"))
console.log(isCircularSentence("eetcode"))
console.log(isCircularSentence("Leetcode is cool"))
