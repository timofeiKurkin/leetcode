type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type ArrayType = { "id": number } & Record<string, JSONValue>;

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {
    const map = {};

    arr1.forEach((item) => map[item.id] = item)

    arr2.forEach((item) => {
        const { id } = item
        map[id] = Object.assign(map[id] || {}, item)
    })

    return Object.values(map)
};