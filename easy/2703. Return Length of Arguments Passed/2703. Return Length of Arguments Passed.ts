type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
    return [...args].length
};

console.log(argumentsLength("a", { "b": 1 }, null, 0, [5]));

export { }