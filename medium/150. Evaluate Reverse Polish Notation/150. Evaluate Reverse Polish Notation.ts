function evalRPN(tokens: string[]): number {
    const operations = new Set(["/", "+", "-", "*"])
    const stack: number[] = []

    for (const element of tokens) {
        if (!operations.has(element))
            stack.push(Number(element))
        else {
            const right = Number(stack.pop())
            const left = Number(stack.pop())

            if (element === "/")
                stack.push(Math.trunc(left / right))

            if (element === "*")
                stack.push(left * right)

            if (element === "-")
                stack.push(left - right)

            if (element === "+")
                stack.push(left + right)
        }
    }

    return stack.pop()!
};


console.log(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

export { }

