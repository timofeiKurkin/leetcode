// 70. Climbing Stairs
// Дано: число n, которое обозначает сколько шагов нужно, чтобы добраться до вершины лестницы. 
// n - всегда означает то, что вы точно будете на вершине и у вас не останется лишних шагов. 
// Можно подниматься по одной ступени или перепрыгивать сразу две.
// Условие: сколькими различными способами можно добраться до вершины лестницы. Т.е. сколько есть комбинаций попасть на вершину.

// Пример 1:
// Вход: n = 2
// Выход: 2
// Пояснение: Есть два способа дойти до вершины. 1 шаг + 1 шаг и сразу 2 шага

// Пример 1:
// Вход: n = 4
// Выход: 2
// Пояснение: Есть пять способов дойти до вершины:
// 1 + 1 + 1 + 1 - понятно
// 1 + 1 + 2
// 1 + 2 + 1
// 2 + 1 + 1
// 2 + 2

// Constraints:
// * 1 <= n <= 45

// Draft: 
// 1. 5 - 1 + 1 + 1 + 1 + 1 | 1 + 1 + 1 + 2 | 1 + 1 + 2 + 1 | 1 + 2 + 1 + 1 | 2 + 1 + 1 + 1 | 1 + 1 + 2 + 2 | 1 + 2 + 2 + 1 ...

const n1 = 3
const n2 = 4
const n3 = 13
const n4 = 27
const n5 = 33

function climbStairs(n: number): number {
    // const upStairs = (step: number): number => {
    //     if(step > n) return 0
    //     if(step === n) return 1

    //     return upStairs(step + 1) + upStairs(step + 2)
    // }
    // return upStairs(0)

    // if (n === 0 || n === 1) return 1
    // let a = 1, // a - количество способов подняться на 2 ступень.
    //     b = 1 // b - количество способов подняться на 1 ступеней. Мы заранее понимаем, что на 1 ступень можно забраться как минимум 1 способом
    // for (let i = 2; i <= n; i++) {
    //     const current = b + a // Количество способов подняться следующую ступень
    //     b = a // Устанавливаем для b предыдущее значение a
    //     a = current // А для a устанавливаем новое
    // }
    // return a

    const run = (step: number): number => {
        if (step > n)
            return 0
        if (step === n)
            return 1
        return run(step + 1) + run(step + 2)
    }

    return run(0)
};

console.log(climbStairs(n1));
console.log(climbStairs(n2));
console.log(climbStairs(n3));
console.log(climbStairs(n4));
console.log(climbStairs(n5));

export { }