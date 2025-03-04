class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        simplify_path = []

        for item in stack:
            if item == "..":
                if simplify_path:
                    simplify_path.pop()

            else:
                if item != "." and item:
                    simplify_path.append(item)

        return "/" + "/".join(simplify_path)


solution = Solution()
print(solution.simplifyPath("/home/"))
print(solution.simplifyPath("/home//foo/"))
print(solution.simplifyPath("/home/user/Documents/../Pictures"))
print(solution.simplifyPath("/../"))
print(solution.simplifyPath("/.../a/../b/c/../d/./"))
