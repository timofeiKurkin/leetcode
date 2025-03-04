function strStr(haystack: string, needle: string): number {
    // let index = 0
    // const needle_length = needle.length
    // while (index < haystack.length) {
    //     const right = index + needle_length
    //     if (haystack.slice(index, right) === needle)
    //         return index
    //     index += 1
    // }
    // return -1

    return haystack.indexOf(needle)
};