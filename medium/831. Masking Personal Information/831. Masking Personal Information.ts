function maskPII(s: string): string {
    s = s.toLowerCase()
    const mailIndex = s.indexOf("@")
    if (s.includes("@")) {
        return s[0] + "*****" + s[mailIndex - 1] + s.slice(mailIndex,)
    }

    const digits = s.split("").filter(d => !Number.isNaN(parseInt(d)))
    const numberFormat = "***-***-" + digits.slice(digits.length - 4).join("")

    if (digits.length === 10) return numberFormat

    return `+${"*".repeat(digits.length - 10)}-` + numberFormat
};