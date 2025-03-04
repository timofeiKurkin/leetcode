from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def run(
            *, tree: Optional[TreeNode], minimum: int, prev: Optional[int]
        ) -> Tuple[Optional[int], int]:
            # if tree.left:
            #     minimum = min(minimum, tree.val - tree.left.val)

            # if tree.right:
            #     minimum = min(minimum, tree.right.val - tree.val)

            # return min(
            #     run(tree=tree.left, minimum=minimum),
            #     run(tree=tree.right, minimum=minimum),
            # )

            if not tree:
                return prev, minimum

            prev, minimum = run(tree=tree.left, minimum=minimum, prev=prev)

            if prev is not None:
                minimum = min(minimum, tree.val - prev)

            prev = tree.val

            return run(tree=tree.right, minimum=minimum, prev=prev)

        _, res = run(tree=root, minimum=float("inf"), prev=None)
        return res


print()
