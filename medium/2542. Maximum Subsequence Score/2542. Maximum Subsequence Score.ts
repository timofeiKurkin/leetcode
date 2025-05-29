class MinHeap {
    private heap: number[] = []

    insert(val: number) {
        this.heap.push(val)
        let i = this.heap.length - 1
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2)
            if (this.heap[i] >= this.heap[parent]) break
                ;[this.heap[i], this.heap[parent]] = [this.heap[parent], this.heap[i]]
            i = parent
        }
    }

    remove(): number | undefined {
        const top = this.heap[0]
        const last = this.heap.pop()
        if (this.heap.length > 0 && last !== undefined) {
            this.heap[0] = last
            this.heapify(0)
        }
        return top
    }

    private heapify(i: number) {
        const n = this.heap.length
        while (true) {
            let smallest = i
            const left = 2 * i + 1, right = 2 * i + 2
            if (left < n && this.heap[left] < this.heap[smallest]) smallest = left
            if (right < n && this.heap[right] < this.heap[smallest]) smallest = right
            if (smallest === i) break
                ;[this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]]
            i = smallest
        }
    }

    peek(): number | undefined {
        return this.heap[0]
    }

    size(): number {
        return this.heap.length
    }
}

function maxScore(nums1: number[], nums2: number[], k: number): number {
    let res = 0
    let prefix = 0
    const hp = new MinHeap()

    const combinations: number[][] = []
    for (let i = 0; i < nums1.length; i++) {
        combinations.push([nums1[i], nums2[i]])
    }
    combinations.sort((a, b) => b[1] - a[1])

    for (const [a, b] of combinations) {
        prefix += a
        hp.insert(a)

        if (hp.size() === k) {
            res = Math.max(res, prefix * b)
            prefix -= hp.remove()!
        }
    }

    return res
};