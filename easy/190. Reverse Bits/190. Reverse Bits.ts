function reverseBits(n: number): number {
    const binary = n.toString(2).padStart(32, "0").split("").reverse().join("")
    const reversedBits = parseInt(binary, 2)
    return reversedBits
};

export { }

