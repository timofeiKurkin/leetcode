from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def run(tree: Optional[TreeNode], path: List[str], res: List[str]) -> List[str]:
            if not tree:
                return

            # path = path + "->" + str(tree.val) if len(path) else str(tree.val)
            path.append(str(tree.val))

            if not tree.left and not tree.right:
                res.append("->".join(path))
            else:
                run(tree.left, path, res)
                run(tree.right, path, res)

            path.pop()

        if not root:
            return []

        res: List[str] = []
        run(root, "", res)
        return res
