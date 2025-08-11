type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    return {
        toBe: function (otherVal) {
            if (otherVal === val) return true;
            throw new Error("Not Equal");
        },
        notToBe: function (otherVal) {
            if (otherVal !== val) return true;
            throw new Error("Equal");
        },
    };
}

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */

export { };
