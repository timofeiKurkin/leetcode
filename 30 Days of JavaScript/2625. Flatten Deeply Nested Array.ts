type MultiDimensionalArray = (number | MultiDimensionalArray)[];

const flat = function (arr: MultiDimensionalArray, n: number): MultiDimensionalArray {
    let newArray: MultiDimensionalArray = []

    arr.forEach((item) => {
        if (Array.isArray(item) && n) {
            for (const flatted of flat(item, n - 1)) {
                newArray.push(flatted)
            }
        } else {
            newArray.push(item)
        }
    })

    return newArray
};
