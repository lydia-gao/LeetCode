# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(node: Optional[TreeNode], cur_max: int) -> int:
            if node is None:
                return 0
            good = 1 if node.val >= cur_max else 0
            new_max = max(cur_max, node.val)
            return good + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, root.val)
