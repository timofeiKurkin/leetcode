type Fn = () => Promise<any>

function promiseAny(promises: Fn[]) {
    return new Promise((resolve, reject) => {
        promises.forEach((promise) => {
            Promise.resolve(promise()).then(resolve, reject)
        })
    })
}

export { }

