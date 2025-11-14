function validMountainArray(arr: number[]): boolean {
    const n = arr.length
    if (n < 3) {
        return false
    }

    let left = 0, right = n - 1

    while (left + 1 < n - 1 && arr[left] < arr[left + 1]) {
        left += 1
    }

    while (right - 1 > 0 && arr[right - 1] > arr[right]) {
        right -= 1
    }

    return right === left
}