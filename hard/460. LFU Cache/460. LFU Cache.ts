class Node {
    constructor(public key: number, public value: number, public freq: number = 1, public prev?: Node, public next?: Node) {
    }
}

class DLinkedList {
    private sentinel: Node
    private size: number

    constructor() {
        this.sentinel = new Node(-1, -1)
        this.sentinel.next = this.sentinel
        this.sentinel.prev = this.sentinel
        this.size = 0
    }

    public push(node: Node) {
        node.next = this.sentinel.next
        node.prev = this.sentinel

        if (node.next?.prev)
            node.next.prev = node

        this.sentinel.next = node
        this.size += 1
    }

    public pop(node?: Node) {
        if (!this.size) {
            return
        }

        if (!node) {
            node = this.sentinel.prev
        }

        if (node) {
            if (node.prev)
                node.prev.next = node.next

            if (node.next)
                node.next.prev = node.prev

            this.size -= 1
        }

        return node
    }
}


class LFUCache {
    private size: number
    private capacity: number
    private node: Record<number, Node>
    private freq: Record<number, DLinkedList>
    private minfreq: number

    constructor(capacity: number) {
        this.size = 0
        this.capacity = capacity
        this.node = {}
        this.freq = { 1: new DLinkedList() }
        this.minfreq = 0
    }

    private update(node: Node) {
        let freq = node.freq

        this.freq[freq]?.pop(node)

        if (this.minfreq === freq && !(freq in this.freq))
            this.minfreq += 1

        node.freq += 1
        freq = node.freq

        if (!(freq in this.freq))
            this.freq[freq] = new DLinkedList()

        this.freq[freq].push(node)
    }

    get(key: number): number {
        if (!(key in this.node)) return -1

        const node = this.node[key]
        this.update(node)
        return node.value
    }

    put(key: number, value: number): void {
        if (!this.capacity) return

        if (key in this.node) {
            const node = this.node[key]
            this.update(node)
            node.value = value
        } else {
            if (this.size == this.capacity) {
                const node = this.freq[this.minfreq].pop()

                if (node)
                    delete this.node[node.key]

                this.size -= 1
            }

            const node = new Node(key, value)
            this.node[key] = node
            this.freq[1].push(node)
            this.minfreq = 1
            this.size += 1
        }
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * var obj = new LFUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

export { }

