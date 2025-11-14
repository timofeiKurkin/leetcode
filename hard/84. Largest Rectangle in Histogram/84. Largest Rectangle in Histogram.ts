function largestRectangleArea(heights: number[]): number {
    // TLE
    // let res = 0
    // for (let i = 0; i < heights.length; i++) {
    //     for (let j = 0; j <= i; j++) {
    //         const nums = heights.slice(j, i + 1)
    //         const minHeight = Math.min(...nums)
    //         res = Math.max(res, minHeight * nums.length)
    //     }
    // }
    // return res

    const n = heights.length
    const stack: number[] = []

    const leftSmaller = new Array<number>(n).fill(0)
    for (let i = 0; i < n; i++) {
        while (stack.length && heights[stack[stack.length - 1]] >= heights[i]) {
            stack.pop()
        }
        leftSmaller[i] = stack.length ? stack[stack.length - 1] : -1
        stack.push(i)
    }

    stack.length = 0

    const rightSmaller = new Array<number>(n).fill(0)
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && heights[stack[stack.length - 1]] >= heights[i]) {
            stack.pop()
        }

        rightSmaller[i] = stack.length ? stack[stack.length - 1] : n
        stack.push(i)
    }

    let res = 0

    for (let i = 0; i < n; i++) {
        const width = rightSmaller[i] - leftSmaller[i] - 1
        res = Math.max(res, heights[i] * width)
    }

    return res
};