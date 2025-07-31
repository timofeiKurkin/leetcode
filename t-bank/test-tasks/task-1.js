// import { InputReader } from "../../inputReader"

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function solve() {
    const input = await readLine();
    const [a, b, c, d] = input.trim().split(" ").map(Number);
    let total = a;
    const traffic = b - d;
    if (traffic < 0) {
        total += Math.abs(traffic) * c;
    }
    console.log(total);
    rl.close();
}
function readLine() {
    return new Promise((res) => {
        rl.once("line", res);
    });
}
solve();


// const fs = require('fs');
// const input = fs.readFileSync(0, 'utf8').trim();
// const [a, b, c, d] = input.split(' ').map(Number);
// let total = a;
// const traffic = b - d;
// if (traffic < 0) {
//     total += Math.abs(traffic) * c;
// }
// console.log(total);
