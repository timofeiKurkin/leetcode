class MyQueue {
    private stack: number[]

    constructor() {
        this.stack = []
    }

    push(x: number): void {
        this.stack = [...this.stack, x]
    }

    pop(): number {
        const topItem = this.stack[0]
        this.stack = this.stack.slice(1,)
        return topItem
    }

    peek(): number {
        if (!this.stack.length) return -1
        return this.stack[0]
    }

    empty(): boolean {
        return !this.stack.length
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */