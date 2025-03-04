// 27. Remove Element
// Дано: массив с разным порядком чисел. Также дан некий val, который является фильтрующим значением.
// Условие: вернуть новую длину массива, после удаления val элементов

const nums1 = [3, 2, 2, 3]
const nums2 = [0, 1, 2, 2, 3, 0, 4, 2]

function removeElement(nums: number[], val: number): number {
    for (let i = 0; i <= nums.length; i++) {
        if (nums[i] === val) {
            nums.splice(i, 1)
            i--
        }
    }
    return nums.length
};


console.log(removeElement(nums1, 3));
console.log(removeElement(nums2, 2));


export { }