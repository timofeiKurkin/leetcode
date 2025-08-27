type Fn<T> = () => Promise<T>

function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {
    return new Promise((resolve, reject) => {
        const results: T[] = [];
        let completed = 0;

        if (!functions.length) {
            return resolve([])
        }

        functions.map((p, index) => {
            Promise.resolve(p()).then(
                value => {
                    results[index] = value;

                    if (++completed === functions.length) {
                        resolve(results)
                    }
                }
            ).catch(err => reject(err))
        })
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */