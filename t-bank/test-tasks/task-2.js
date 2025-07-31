const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function solve() {
    const input = await readLine();
    const parts = parseInt(input.trim());
    let curr = 1;
    let i = 0;

    while (curr < parts) {
        curr *= 2;
        i += 1;
    }

    console.log(i);
    rl.close();
}

function readLine() {
    return new Promise((res) => {
        rl.once("line", res);
    });
}

solve();
