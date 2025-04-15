function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    let i = 0, j = 0
    let first = 0, second = 0
    const n = nums1.length + nums2.length
    const middle = Math.floor(n / 2)

    for (let p = 0; p <= middle; p++) {
        first = second

        if (i < nums1.length && (j >= nums2.length || nums1[i] < nums2[j])) {
            second = nums1[i]
            i += 1
        } else {
            second = nums2[j]
            j += 1
        }
    }

    if (n % 2 === 0)
        return (first + second) / 2

    return second
};

export { }

