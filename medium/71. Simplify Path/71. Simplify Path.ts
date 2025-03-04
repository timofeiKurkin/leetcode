function simplifyPath(path: string): string {
    const splittedPath = path.split("/")
    const simplifyPath: string[] = []

    for (const item of splittedPath) {
        if (item === "..") {
            if (simplifyPath.length)
                simplifyPath.pop()
        } else {
            if (item != "." && item)
                simplifyPath.push(item)
        }
    }

    return "/" + simplifyPath.join("/")
};