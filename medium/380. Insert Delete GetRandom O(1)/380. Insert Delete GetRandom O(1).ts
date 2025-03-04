class RandomizedSet {
    lst: number[]
    indices: { [key in number]: number }

    constructor() {
        this.lst = []
        this.indices = {}
    }

    insert(val: number): boolean {
        if (val in this.indices)
            return false

        const newSize = this.lst.push(val)
        this.indices[val] = newSize - 1
        return true
    }

    remove(val: number): boolean {
        if (!(val in this.indices))
            return false

        const idxToRemove = this.indices[val]
        const lastElement = this.lst[this.lst.length - 1]

        this.lst[idxToRemove] = lastElement
        this.indices[lastElement] = idxToRemove

        this.lst.pop()
        delete this.indices[val]
        return true
    }

    getRandom(): number {
        return this.lst[Math.floor(Math.random() * this.lst.length)]
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */