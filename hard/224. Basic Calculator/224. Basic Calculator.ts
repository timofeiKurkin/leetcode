function calculate(s: string): number {
    const stack: number[] = []
    let result = 0
    let prevNumber = 0
    let sign = 1 // "+" = 1; "-" = -1;

    const updateResult = (): number => result + sign * prevNumber

    for (const element of s) {
        if (!isNaN(Number.parseInt(element))) {
            prevNumber = prevNumber * 10 + Number.parseInt(element)
        }

        else if (element === "+" || element === "-") {
            result = updateResult()
            prevNumber = 0
            sign = element === "+" ? 1 : -1
        }

        else if (element === "(") {
            stack.push(result)
            stack.push(sign)
            result = 0
            sign = 1
        }

        else if (element === ")") {
            result = updateResult()
            prevNumber = 0
            result *= stack.pop()!
            result += stack.pop()!
        }
    }

    result = updateResult()
    return result
};

console.log(calculate("1 + 1"))
console.log(calculate(" 2-1 + 2 "))
console.log(calculate("(1+(4+5+2)-3)+(6+8)"))
console.log(calculate("2147483647"))
console.log(calculate("1-(     -2)"))
console.log(calculate("-2+ 1"))
console.log(calculate("- (3 + (4 + 5))"))

export { }

