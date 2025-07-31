const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
async function solve() {
    const input = await readLine();
    // 1 <= n, m <= 31
    const [n, m] = input.split(" ").map(Number)
    if (n <= 7) {
        console.log(m + (n + Math.abs(n - 7)))
    } else {
        console.log(n - 7)
    }

    rl.close()
}
function readLine() {
    return new Promise((res) => {
        rl.once("line", res);
    });
}

solve();
