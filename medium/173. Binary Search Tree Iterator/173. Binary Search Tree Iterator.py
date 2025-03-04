from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # def transform_tree(tree: Optional[TreeNode]) -> List[int]:
        #     if not tree:
        #         return []

        #     return transform_tree(tree.left) + [tree.val] + transform_tree(tree.right)

        # self.tree_arr = transform_tree(root)
        # self.curr_index = 0
        
        self.stack: List[TreeNode] = []
        self.left_most_in_order(root)

    def left_most_in_order(self, tree: Optional[TreeNode]):
        while tree:
            self.stack.append(tree)
            tree = tree.left
    
    def next(self) -> int:
        top_of_stack = self.stack.pop()
        if top_of_stack.right:
            self.left_most_in_order(top_of_stack.right)
        return top_of_stack.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
