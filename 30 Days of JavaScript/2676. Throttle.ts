type F = (...args: any[]) => void;

const throttle = (fn: F, t: number): F => {
    let isPending = false

    return function (...args) {
        if (isPending) {
            return
        }

        isPending = true

        setTimeout(() => {
            isPending = false
        }, t)

        fn.apply(this, args)
    }
}