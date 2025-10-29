function smallestNumber(n: number): number {
    return parseInt(n.toString(2).split("").map(i => i === "0" ? "1" : i).join(""), 2)
};
