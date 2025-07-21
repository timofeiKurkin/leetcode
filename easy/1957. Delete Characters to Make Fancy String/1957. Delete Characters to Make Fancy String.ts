function makeFancyString(s: string): string {
    // const res = s.slice(0, 2).split("")
    let res = ""
    let prevOne = res[0]
    let prevTwo = res[1]

    for (const sym of s) {
        if (prevOne === prevTwo && prevOne === sym) {
            continue
        }

        prevOne = prevTwo
        prevTwo = sym
        res += sym
    }

    return res
};