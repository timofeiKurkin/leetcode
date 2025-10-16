function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    const stack: number[] = [], map = new Map<number, number>()

    for (const num of nums2) {
        while (stack.length && num > stack[stack.length - 1]) {
            map.set(stack.pop()!, num)
        }
        stack.push(num)
    }

    for (const num of stack) {
        map.set(num, -1)
    }

    return nums1.map(n => map.get(n) || -1)
};