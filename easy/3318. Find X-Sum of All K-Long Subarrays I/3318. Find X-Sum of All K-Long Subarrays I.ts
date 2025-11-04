function findXSum(nums: number[], k: number, x: number): number[] {
    return solution2(nums, k, x)
};

function solution1(nums: number[], k: number, x: number): number[] {
    function xSum(nums: number[], x: number): number {
        const freq: Record<number, number> = {}
        for (const num of nums) {
            freq[num] = (freq[num] || 0) + 1
        }

        return Object.entries(freq)
            .sort((a, b) => b[1] === a[1] ? Number(b[0]) - Number(a[0]) : b[1] - a[1])
            .slice(0, x)
            .reduce((acc, [num, freq]) => acc += (Number(num) * freq), 0)
    };

    const res: number[] = []

    for (let i = 0; i <= nums.length - k; i++) {
        res.push(xSum(nums.slice(i, i + k), x))
    }

    return res
}

function solution2(nums: number[], k: number, x: number): number[] {
    function xSum(freq: number[][]): number {
        const freqSorted = freq.toSorted((a, b) => b[1] - a[1])
        console.log(freqSorted)
        let sum = 0
        for (let i = 0; i <= freqSorted.length - x; i++) {
            const [num, f] = freqSorted[i]
            if (!f) break
            sum += (num * f)
        }
        return sum
    }

    const n = nums.length
    const sz = n - k + 1
    const res = new Array<number>(sz).fill(0)
    const freq = Array.from({ length: 51 }, () => [0, 0])

    for (let i = 0; i < sz; i++) {
        const z = nums[i]
        freq[z][0] = z
        freq[z][1] += 1
    }

    res[0] = xSum(freq)

    for (let i = 1; i < sz; i++) {
        const l = nums[i - 1], r = nums[i + k - 1]
        freq[l][0] -= 1
        freq[r][0] += 1
        freq[r][1] = r
        res[i] = xSum(freq)
    }

    return res
}