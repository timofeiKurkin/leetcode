function lengthOfLastWord(s: string): number {
    // const res = s.split(" ")
    //     // .filter((item) => /^[a-zA-Z0-9]*$/.test(item))
    //     .filter(Boolean)
    // console.log(res)
    // console.log(res.slice())
    // return res.slice(0, -1).length

    const items = s.split(" ").filter(Boolean)

    if (!items.length)
        return 0

    const lastItem = items.pop()!
    return lastItem.length
};

console.log(lengthOfLastWord("Hello World"))
console.log(lengthOfLastWord("   fly me   to   the moon  "))
console.log(lengthOfLastWord("luffy is still joyboy"))
