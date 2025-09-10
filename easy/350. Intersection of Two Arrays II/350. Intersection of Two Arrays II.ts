function intersect(nums1: number[], nums2: number[]): number[] {
    return solution3(nums1, nums2)
};

function solution1(nums1: number[], nums2: number[]): number[] {
    // Brute force
    const ht1: { [key in number]: number } = {}
    const ht2: { [key in number]: number } = {}

    for (const num of nums1) {
        ht1[num] = (ht1[num] || 0) + 1
    }

    for (const num of nums2) {
        ht2[num] = (ht2[num] || 0) + 1
    }

    const res: number[] = []

    for (const num in ht1) {
        if (num in ht1) {
            for (let i = 0; i < Math.min(ht1[num], ht2[num]); i++) {
                res.push(Number(num))
            }
        }
    }

    return res
}

function solution2(nums1: number[], nums2: number[]): number[] {
    const counter: { [key in number]: number } = {}
    const res: number[] = []

    for (const num of nums1) {
        counter[num] = (counter[num] || 0) + 1
    }

    for (const num of nums2) {
        if (counter[num]) {
            res.push(num)
            counter[num] -= 1
        }
    }

    return res
}

function solution3(nums1: number[], nums2: number[]): number[] {
    nums1.sort((a, b) => a - b);
    nums2.sort((a, b) => a - b);

    const res: number[] = []
    let i = 0, j = 0

    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] > nums2[j]) {
            j += 1
        } else if (nums1[i] < nums2[j]) {
            i += 1
        } else {
            res.push(nums1[i])
            i += 1
            j += 1
        }
    }

    return res
}