function eatenApples(apples: number[], days: number[]): number {
    class MinHeap<T extends Array<number>> {
        private heap: T[] = [];

        push(val: T): void {
            this.heap.push(val);
            this.heapifyUp();
        }

        pop(): T | undefined {
            if (this.heap.length === 0) return undefined;
            this.swap(0, this.heap.length - 1);
            const min = this.heap.pop();
            this.heapifyDown();
            return min;
        }

        peek(): T | undefined {
            return this.heap[0];
        }

        size(): number {
            return this.heap.length
        }

        private heapifyUp(): void {
            let index = this.heap.length - 1;
            while (index > 0) {
                const parent = Math.floor((index - 1) / 2);

                if (this.heap[parent][0] <= this.heap[index][0]) break;
                this.swap(index, parent);
                index = parent;
            }
        }

        private heapifyDown(): void {
            let index = 0;
            const length = this.heap.length;

            while (true) {
                let smallest = index;
                const left = 2 * index + 1;
                const right = 2 * index + 2;

                if (left < length && this.heap[left][0] < this.heap[smallest][0]) {
                    smallest = left;
                }

                if (right < length && this.heap[right][0] < this.heap[smallest][0]) {
                    smallest = right;
                }

                if (smallest === index) break;
                this.swap(index, smallest);
                index = smallest;
            }
        }

        private swap(i: number, j: number): void {
            [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
        }
    }


    const heapq = new MinHeap<[number, number]>()

    const n = apples.length
    let i = 0
    let res = 0

    while (i < n || heapq.size()) {
        if (i < n && apples[i] > 0) {
            heapq.push([i + days[i], apples[i]])
        }

        let peak = heapq.peek()

        while (peak && heapq.size() && (peak[0] <= i || peak[1] === 0)) {
            heapq.pop()
        }

        peak = heapq.peek()

        if (peak && heapq.size()) {
            peak[1] -= 1
            res += 1
        }

        i += 1
    }

    return res
};

export { };

