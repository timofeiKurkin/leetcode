function minimumTeachings(n: number, languages: number[][], friendships: number[][]): number {
    const userToTeach = new Set<number>()

    for (const [u, v] of friendships) {
        const user = u - 1
        const friend = v - 1
        let canCommunicate = false

        for (const lang of languages[user]) {
            if (languages[friend].includes(lang)) {
                canCommunicate = true
                break
            }
        }

        if (!canCommunicate) {
            userToTeach.add(user)
            userToTeach.add(friend)
        }
    }

    let minUsersToTeach = languages.length + 1;

    for (let language = 1; language <= n; language++) {
        let count = 0
        for (const user of userToTeach) {
            if (!languages[user].includes(language)) {
                count += 1
            }
        }
        minUsersToTeach = Math.min(minUsersToTeach, count)
    }

    return minUsersToTeach
};
