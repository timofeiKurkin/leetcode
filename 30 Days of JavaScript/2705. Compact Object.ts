type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function compactObject(obj: Obj): Obj {
    return solution2(obj)
};

function solution1(obj: Obj) {
    // In place
    if (Array.isArray(obj)) {
        let i = 0

        while (i < obj.length) {
            const item = obj[i]
            if (Array.isArray(item)) {
                compactObject(item)
                i += 1
            } else if (item === null || !Boolean(item)) {
                obj.splice(i, 1)
            } else if (typeof item === "object") {
                compactObject(item)
                i += 1
            } else {
                i += 1
            }
        }
    } else {
        for (const key in obj) {
            if (Array.isArray(obj[key])) {
                compactObject(obj[key])
            } else {
                const item = obj[key]
                if (item === null || !Boolean(item)) {
                    delete obj[key]
                } else if (typeof item === "object") {
                    compactObject(item)
                }
            }
        }
    }

    return obj
}

function solution2(obj: Obj) {
    // JSON Arrays
    if (Array.isArray(obj)) {
        const result: JSONValue[] = [];
        for (const val of obj) {
            if (typeof val === 'object' && val !== null) {
                result.push(compactObject(val));
            }
            else if (val) result.push(val);
        }
        return result;
    }

    // JSON Objects
    for (const key in obj) {
        if (typeof obj[key] === 'object' && obj[key] !== null) {
            obj[key] = compactObject(obj[key]);
        }
        else if (!obj[key]) {
            delete obj[key];
        }
    }

    return obj;
}