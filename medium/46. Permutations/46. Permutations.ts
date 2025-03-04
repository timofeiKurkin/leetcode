function permute(nums: number[]): number[][] {
    function backtrack(path: number[], rem: number[]) {
        if (!rem.length) {
            res.push(path)
            return
        }
        for (let i = 0; i < rem.length; i++) {
            backtrack(path.concat([rem[i]]), rem.slice(0, i).concat(rem.slice(i + 1,)))
        }

    }
    const res: number[][] = []
    backtrack([], nums)
    return res
};

console.log(permute([1, 2, 3]))
console.log(permute([1, 2, 3, 4, 6]))
console.log(permute([0, 1]))
console.log(permute([1]))
