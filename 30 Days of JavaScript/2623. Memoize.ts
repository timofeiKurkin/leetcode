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

