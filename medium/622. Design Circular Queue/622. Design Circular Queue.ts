class MyCircularQueue {
    queue: number[]
    capacity: number
    head: number
    n: number

    constructor(k: number) {
        this.queue = new Array(k).fill(0)
        this.capacity = k
        this.head = 0
        this.n = 0
    }

    enQueue(value: number): boolean {
        if (this.n === this.capacity) return false

        const index = (this.head + this.n) % this.capacity
        this.queue[index] = value
        this.n += 1
        return true
    }

    deQueue(): boolean {
        if (!this.n) return false

        this.head = (this.head + 1) % this.capacity
        this.n -= 1
        return true
    }

    Front(): number {
        if (!this.n) return -1
        return this.queue[this.head]
    }

    Rear(): number {
        if (!this.n) return -1

        const tail = (this.head + this.n - 1) % this.capacity
        return this.queue[tail]
    }

    isEmpty(): boolean {
        return !this.n
    }

    isFull(): boolean {
        return this.n === this.capacity
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */