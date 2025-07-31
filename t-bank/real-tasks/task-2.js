const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
async function solve() {
    const input = await readLine();
    // Дано: строка s с английскими буквами: 1 <= s.length <= 10^5
    // Найти количество троек (i; j; k) так, что:
    // i < j < k и s[i] =<< a >>, s[j] =<< b >>, s[k] =<< c >>
    const s = input.trim() + ""
    
    if (s.length < 3) {
        console.log(0)
    } else {
        let countA = 0
        let countAB = 0
        let result = 0
        for (const symbol of s) {
            if (symbol === "a") {
                countA += 1
            } else if (symbol === "b") {
                countAB += countA
            } else {
                result += countAB
            }
        }
        console.log(result)
    }

    rl.close()
}
function readLine() {
    return new Promise((res) => {
        rl.once("line", res);
    });
}

solve();
