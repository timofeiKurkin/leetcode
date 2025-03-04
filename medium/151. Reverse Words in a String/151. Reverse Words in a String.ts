function reverseWords(s: string): string {
    if (!s.length)
        return ""
    // let a = s.trim().split(" ").filter(Boolean)
    // return a.reverse().join(" ")

    s = s.trim();
    return s.split(/\s+/).reverse().join(' ');
};


const s_1 = "the sky is blue"
const s_2 = "  hello world  "
const s_3 = "a good   example"

console.log(reverseWords(s_1))
console.log(reverseWords(s_2))
console.log(reverseWords(s_3))