type Timeout = ReturnType<typeof setTimeout>

class TimeLimitedCache {
    timeous: Map<number, Timeout>
    items: Map<number, number>
    constructor() {
        this.timeous = new Map<number, Timeout>()
        this.items = new Map<number, number>()
    }

    set(key: number, value: number, duration: number): boolean {
        const recordExists = this.items.has(key)

        if (recordExists) {
            clearTimeout(this.timeous.get(key))
        }

        this.items.set(key, value)
        const timerId = setTimeout(() => this.items.delete(key), duration)
        this.timeous.set(key, timerId)
        return recordExists
    }

    get(key: number): number {
        return this.items.get(key) || -1
    }

    count(): number {
        return this.items.size
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */