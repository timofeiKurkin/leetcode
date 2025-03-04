function spiralOrder(matrix: number[][]): number[] {
    let res: number[] = []
    let top = 0, bottom = matrix.length - 1, left = 0, right = matrix[0].length - 1
    let direction_index = 0 // 0 - вправо; 1 - вниз; 2 - влево; 3 - вверх

    while (top <= bottom && left <= right) {
        if (direction_index === 0) {
            res = res.concat(matrix[top].slice(left, right + 1))
            top += 1
        } else if (direction_index === 1) {
            for (let i = top; i < bottom + 1; i++) {
                res.push(matrix[i][right])
            }
            right -= 1
        } else if (direction_index === 2) {
            res = res.concat(matrix[bottom].slice(left, right + 1).reverse())
            bottom -= 1
        } else if (direction_index === 3) {
            for (let i = bottom; i > top - 1; i--) {
                res.push(matrix[i][left])
            }
            left += 1
        }

        direction_index = (direction_index + 1) % 4
    }

    return res
};

console.log(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
console.log(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
console.log(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [12, 23, 34, 45], [9, 10, 11, 12]]))

export { }

