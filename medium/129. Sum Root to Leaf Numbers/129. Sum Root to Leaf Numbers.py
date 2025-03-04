from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # def collect_paths(
        #     tree: Optional[TreeNode], path: str, paths: List[int]
        # ) -> None:
        #     if not tree:
        #         return

        #     path = path + str(tree.val)

        #     if not tree.left and not tree.right:
        #         paths.append(int(path))
        #     else:
        #         collect_paths(tree.left, path, paths)
        #         collect_paths(tree.right, path, paths)

        #     path = path[: len(path) - 1]

        # paths = []
        # collect_paths(root, "", paths)

        # return sum(paths)
        
        def dfs(tree: Optional[TreeNode], curr_number: int) -> int:
            if not tree:
                return 0
            
            curr_number = curr_number * 10 + tree.val
            
            if not tree.right and not tree.left:
                return curr_number
            
            return dfs(tree.left, curr_number) + dfs(tree.right, curr_number)
        
        return dfs(root, 0)


solution = Solution()
# print(solution.sumNumbers(root=[1, 2, 3]))
# print(solution.sumNumbers(root=[4, 9, 0, 5, 1]))
print("123"[:2])
