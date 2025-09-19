class Spreadsheet {
    spreadsheet: Map<string, number[]>

    constructor(rows: number) {
        this.spreadsheet = new Map()
    }

    private parseCell(cell: string): [string, number] {
        return [cell.slice(0, 1), parseInt(cell.slice(1,))]
    }

    setCell(cell: string, value: number): void {
        const [column, row] = this.parseCell(cell)

        const columnData = this.spreadsheet.get(column) || []

        columnData[row] = value
        this.spreadsheet.set(column, columnData)
    }

    resetCell(cell: string): void {
        this.setCell(cell, 0)
    }

    getValue(formula: string): number {
        const operants = formula.slice(1,).split("+")

        let res = 0;

        for (const operant of operants) {
            if (/[A-Z]/.test(operant[0])) {
                const [column, row] = this.parseCell(operant)
                const columnData = this.spreadsheet.get(column) || []

                if (row < columnData.length) {
                    res += columnData[row] || 0
                }
            } else {
                res += parseInt(operant)
            }
        }

        return res
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * var obj = new Spreadsheet(rows)
 * obj.setCell(cell,value)
 * obj.resetCell(cell)
 * var param_3 = obj.getValue(formula)
 */

const obj = new Spreadsheet(5)
// obj.setCell("U558", 17217)
// obj.getValue("=59437+H286")
// obj.setCell("C164", 67231)
// obj.setCell("Y294", 75466)
// obj.getValue("=Y169+Y294")
// obj.getValue("F154")
