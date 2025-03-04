function maxArea(height: number[]): number {
    let left = 0, right = height.length - 1
    let maxSquare = 0

    while (left < right) {
        maxSquare = Math.max(maxSquare, Math.min(height[left], height[right]) * (right - left))

        if (height[left] < height[right])
            left += 1
        else
            right -= 1
    }

    return maxSquare
};

export { }