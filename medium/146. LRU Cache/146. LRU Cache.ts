class LRUCache {
    cache: Map<number, number>
    capacity: number

    constructor(capacity: number) {
        this.cache = new Map()
        this.capacity = capacity
    }

    get(key: number): number {
        if (!this.cache.has(key))
            return -1

        const value = this.cache.get(key)!
        this.cache.delete(key)
        this.cache.set(key, value)

        return value
    }

    put(key: number, value: number): void {
        if (this.cache.has(key)) {
            this.cache.delete(key)
        }

        this.cache.set(key, value)

        if (this.cache.size > this.capacity) {
            const firstKey = this.cache.keys().next().value!
            this.cache.delete(firstKey)
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

console.log(Object.keys({ 1: 1, 2: 2, 3: 3 }))
console.log(Object.keys({ 3: 3, 2: 2, 1: 1 }))