function convert(s: string, numRows: number): string {
    if (s.length === 1 || numRows === 1)
        return s

    let is_going_down = true
    let curr_row = 0
    const rows = Array(numRows).fill("")

    for (const char of s) {
        rows[curr_row] += char

        if (curr_row === 0 || curr_row === numRows - 1) {
            is_going_down = !is_going_down
        }

        curr_row += !is_going_down ? 1 : -1
    }

    return rows.join("")
};

console.log(convert("PAYPALISHIRING", 3))
// console.log(convert("PAYPALISHIRING", 4))
// console.log(convert("A", 1))