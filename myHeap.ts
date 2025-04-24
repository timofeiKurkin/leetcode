export class MinHeap {
    private heap: number[] = [];

    push(val: number): void {
        this.heap.push(val);
        this.heapifyUp();
    }

    pop(): number | undefined {
        if (this.heap.length === 0) return undefined;
        this.swap(0, this.heap.length - 1);
        const min = this.heap.pop();
        this.heapifyDown();
        return min;
    }

    peek(): number | undefined {
        return this.heap[0];
    }

    private heapifyUp(): void {
        let index = this.heap.length - 1;
        while (index > 0) {
            const parent = Math.floor((index - 1) / 2);
            if (this.heap[parent] <= this.heap[index]) break;
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

            if (left < length && this.heap[left] < this.heap[smallest]) {
                smallest = left;
            }

            if (right < length && this.heap[right] < this.heap[smallest]) {
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

export { };

