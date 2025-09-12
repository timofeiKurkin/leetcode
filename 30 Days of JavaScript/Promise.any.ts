type Fn = Promise<any>

function promiseAny(promises: Fn[]) {
    const errors: any[] = []

    return new Promise((resolve, reject) => {
        promises.forEach((promise) => {
            promise.then((res) => resolve(res)).catch((err) => {
                const newLength = errors.push(err)

                if (newLength === promises.length) {
                    reject(errors)
                }
            })
        })
    })
}

const resolve = <T>(data: T, time: number) => new Promise((res) => setTimeout(() => res(data), time))
const reject = <T>(data: T, time: number) => new Promise((_, rej) => setTimeout(() => rej(data), time))

const firstList = [resolve(1, 220), resolve(2, 199), resolve(3, 200), resolve(4, 500)]
console.log(promiseAny(firstList).then((res) => console.log(res)))

export { }
