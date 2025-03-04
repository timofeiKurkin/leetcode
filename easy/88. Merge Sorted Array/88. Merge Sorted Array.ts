// Дано: два отсортированных в порядке возрастания массива и два числа: m и n. Число n указывает, сколько нулей в nums1. Он также показывает сколько элементов в nums2.
// Условие: соединить массив nums1 и nums2 методом "замены на месте". nums1 будет отсортированным и включать все элементы nums2. Ничего не возвращать.

/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let a = m - 1 // index only for nums1 array 
    let c = m + n - 1 // index for both arrays ((m + n) - 1)

    let b = n - 1 // index only for nums2 array

    while (b >= 0) {
        if (a >= 0 && nums1[a] > nums2[b]) {
            nums1[c] = nums1[a]
            a -= 1
        } else {
            nums1[c] = nums2[b]
            b -= 1
        }
        c -= 1
    }

    console.log(nums1)
};


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
merge([2, 0], 1, [1], 1)
merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)

