

const promisePool = async function (functions: Function[], n: number): Promise<void> {
    return new Promise((res) => {
        let inProgress = 0, index = 0

        function run() {
            if (index >= functions.length) {
                if (inProgress === 0) res()
                return
            }
        }

        while (inProgress < n && index < functions.length) {
            inProgress++
            functions[index++]().then(() => {
                inProgress--
                run()
            })
        }

        run()
    })
}