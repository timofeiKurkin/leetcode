function doesAliceWin(s: string): boolean {
    for (const char of s) {
        if ("aeuio".includes(char)) {
            return true
        }
    }
    return false
};