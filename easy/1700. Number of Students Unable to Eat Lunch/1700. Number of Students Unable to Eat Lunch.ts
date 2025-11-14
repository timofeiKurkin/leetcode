function countStudents(students: number[], sandwiches: number[]): number {
    const counter: Record<number, number> = {}

    for (const student of students) {
        counter[student] = (counter[student] || 0) + 1
    }

    while (students.length && counter[sandwiches[0]]) {
        const student = students.shift()!

        if (sandwiches[0] === student) {
            sandwiches.shift()
            counter[student] = (counter[student] || 0) - 1
        } else {
            students.push(student)
        }
    }

    return students.length
};

// b = 1,0,0,0,1,1
// s = 1,1,1,0,0,1

// 1
// b = 0,0,0,1,1
// s = 1,1,0,0,1

// 2
// b = 0,0,0,1,1
// s = 1,0,0,1,1

// 3
// b = 0,0,0,1,1
// s = 0,0,1,1,1

// 4-5
// b = 0,1,1
// s = 1,1,1

// 6
// answer s.length, because there is no 0 in students