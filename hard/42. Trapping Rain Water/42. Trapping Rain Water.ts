function trap(height: number[]): number {
    // let maxHeight = 0
    // let width = 0

    // for (let i = 0; i < height.length; i++) {
    //     if (height[i] > maxHeight) maxHeight = height[i]
    //     width += 1
    // }

    // let area = maxHeight * width

    // for (let i = 0; i < height.length; i++) {
    //     if (i || height[i]) {
    //         if (height[i] > height[i + 1]) {
    //             area -= (maxHeight - height[i + 1])
    //         } else if (height[i] <= height[i + 1] && height[i + 1] <= maxHeight) {
    //             area -= (maxHeight - height[i + 1])
    //         } else {
    //             if (i === height.length - 1 && height[i] < maxHeight) {
    //                 // width -= 1
    //                 // console.log(width)
    //                 // area -= (width + (maxHeight - height[i]))
    //             }
    //         }
    //     } else {
    //         area -= maxHeight
    //     }
    // }
    // return area

    let left = 0, right = height.length - 1
    let leftMax = 0, rightMax = 0
    let res = 0

    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] > leftMax) {
                leftMax = height[left]
            } else {
                res += leftMax - height[left]
            }

            left++
        } else {
            if (height[right] > rightMax) {
                rightMax = height[right]
            } else {
                res += rightMax - height[right]
            }
            right--
        }
    }

    return res

    // let res = 0
    // let maxHeight = 0
    // let minHeight = 0
    // let width = 1

    // for (let i = 0; i < height.length; i++) {
    //     if (i || height[i]) {
    //         if (height[i] > height[i + 1]) {
    //             if(!maxHeight) maxHeight = height[i]
    //             res += (maxHeight - height[i + 1])
    //             width += 1
    //         } else if (height[i] <= height[i + 1] && height[i + 1] <= maxHeight) {
    //             if(!minHeight) minHeight = height[i]

    //             res += (maxHeight - height[i + 1])
    //             width += 1
    //         } else {
    //             if(i === height.length - 1 && height[i] < maxHeight) {
    //                 width -= 1
    //                 console.log(width)
    //                 res -= (width + (maxHeight - height[i]))
    //             }

    //             maxHeight = 0
    //             minHeight = 0
    //             width = 0
    //         }
    //     }
    // }
    // return res
};


console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
console.log(trap([4, 2, 0, 3, 2, 5]))
console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 2]))
console.log(trap([5, 4, 1, 2]))