type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const ht = new Map<string, number>()
    return function (...args) {
        const htValue = ht.get(args.toString())
        if (htValue !== undefined) {
            return htValue
        }

        const res = fn(...args)
        ht.set(args.toString(), res)
        return res
    }
}

// function memoize(fn: Fn): Fn & { clearCache: () => void } {
//     // ht: ...args, res
//     // ht.has(args) -> res
//     // ht.set(args) -> res
//     const ht = new Map()

//     function memoized(...args: number[]) {
//         if (ht.has(args.toString())) {
//             return ht.get(args.toString())
//         }

//         const res = fn(...args)
//         ht.set(args.toString(), res)
//         return res
//     }

//     memoized.clearCache = () => {
//         ht.clear()
//     }

//     return memoized
// }

// const memoizedFn = memoize((n: number) => n + 1)
// memoizedFn(1)
// memoizedFn.clearCache()


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */

export { }

