const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
async function solve() {
    // Мальчик подошел к лестнице. C каждой ступенькой на ней у него ассоциирован какой-то момент из жизни, который при воспоминании изменит его текущее настроение на a[i]. Мальчик умеет перешагивать на следующую ступеньку, либо перепрыгивать через ступеньку. Еще мальчик умеет абстрагироваться от воспоминаний и проходить вперед на любое количество ступенек, не изменяя свое настроение (в том числе и оказаться на последней ступеньке), но так как он еще недостаточно взрослый, он может сделать это не более k раз. Какое максимальное настроение он может получить, оказавшись на последней ступеньке?
    // Изначально мальчик стоит перед первой ступенькой (не на ней)

    // Дано:
    // n = (1 <= n <= 1000) | k = (0 <= k <= 100)
    // const [n, k] = (await readLine()).trim().split(" ").map(Number);

    // // |a[i]| <= 100 - изменение настроения, если наступить на i-ю ступеньку (снизу вверх)
    // const numbers = (await readLine()).trim().split(" ").map(Number);


    // function run(index, total, k_remind) {
    //     if (index > n) {
    //         return -(10 ** 10)
    //     }

    //     if (index === n) {
    //         return total;
    //     }

    //     if (!k_remind) {
    //         return Math.min(run(index + 1, total + numbers[index], 0), run(index + 2, total + numbers[index], 0));
    //     }

    //     return Math.max(
    //         run(index + 2, total + numbers[index], k_remind),
    //         run(index + 2, total, k_remind - 1),
    //         run(index + 1, total, k_remind - 1),
    //         run(index + 1, total + numbers[index], k_remind)
    //     );
    // }

    // console.log(run(0, 0, k));

    const [n, k] = (await readLine()).trim().split(" ").map(Number);
    const a = (await readLine()).trim().split(" ").map(Number);

    const dp = Array.from({ length: n }, () => Array(k + 1).fill(-Infinity));
    dp[0][0] = a[0];

    for (let i = 0; i < n; i++) {
        for (let used = 0; used <= k; used++) {
            if (dp[i][used] === -Infinity) continue;

            if (i + 1 < n)
                dp[i + 1][used] = Math.max(dp[i + 1][used], dp[i][used] + a[i + 1]);

            if (i + 2 < n)
                dp[i + 2][used] = Math.max(dp[i + 2][used], dp[i][used] + a[i + 2]);

            if (used < k) {
                for (let j = i + 1; j < n; j++) {
                    dp[j][used + 1] = Math.max(dp[j][used + 1], dp[i][used]);
                }
            }
        }
    }

    let res = -Infinity;
    for (let used = 0; used <= k; used++) {
        res = Math.max(res, dp[n - 1][used]);
    }
    console.log(res);

    rl.close();
}
function readLine() {
    return new Promise((res) => {
        rl.once("line", res);
    });
}

solve();
