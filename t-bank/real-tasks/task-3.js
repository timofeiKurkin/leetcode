const readline = require("readline");

class Node {
    constructor(value) {
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
async function solve() {
    // Вам дана последовательность A, изначально состоящая из одного элемента 0 (A = (0)) и строка S длины N, состоящая только из символов "L" и "R"
    // Затем вы проделаете следующую операцию для i = 1, 2, 3, ... N:
    // Если S[i] = "L", то вы вставите число i слева от числа i - 1 в последовательность A
    // Если S[i] = "R", то вы вставите число i справа от числа i - 1 в последовательность A
    // Найти последовательность после операции

    // S[1]​ = L, вы вставите 1 слева от 0. (0)→(1,0)
    // S[2] = R, вы вставите 2 справа от 1. (1,0)→(1,2,0)
    // S[3] = R, вы вставите 3 справа от 2. (1,2,0)→(1,2,3,0)
    // S[4] = R, вы вставите 4 справа от 3. (1,2,3,0)→(1,2,3,4,0)
    // S[5] = L, вы вставите 5 слева от 4. (1,2,3,4,0)→(1,2,3,5,4,0)
    
    // n (1 <= N <= 5 * 10^5)
    const n = parseInt((await readLine() + "").trim())

    // s.length = n и состоит из "L" и "R"
    const s = (await readLine() + "").trim()

    // let A = [0]
    // let prevIndex = 1

    // for (let i = 0; i < n; i++) {
    //     if (s[i] == "R") {
    //         A = [...A.slice(0, prevIndex), i+1, ...A.slice(prevIndex)]
    //         prevIndex += 1
    //     } else {
    //         A = [...A.slice(0, prevIndex-1), i+1, ...A.slice(prevIndex-1)]
    //     }
    // }

    // console.log(A.join(" "))

    let head = new Node(0);
    let tail = head;

    const nodeMap = new Map();
    nodeMap.set(0, head);

    for (let i = 1; i <= n; i++) {
        const prevValue = i - 1;
        const prevNode = nodeMap.get(prevValue);

        const newNode = new Node(i);
        nodeMap.set(i, newNode);

        if (s[i-1] === "R") {
            newNode.prev = prevNode;
            newNode.next = prevNode.next;

            if (prevNode.next) {
                prevNode.next.prev = newNode;
            } else {
                tail = newNode;
            }
            prevNode.next = newNode;
        } else {
            newNode.next = prevNode;
            newNode.prev = prevNode.prev;

            if (prevNode.prev) {
                prevNode.prev.next = newNode;
            } else {
                head = newNode;
            }
            prevNode.prev = newNode;
        }
    }

    const A = [];
    let currentNode = head;
    while (currentNode) {
        A.push(currentNode.value);
        currentNode = currentNode.next;
    }

    console.log(A.join(" "));

    rl.close()
}
function readLine() {
    return new Promise((res) => {
        rl.once("line", res);
    });
}

solve();
