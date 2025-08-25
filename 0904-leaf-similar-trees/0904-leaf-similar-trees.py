# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect(root: Optional[TreeNode], out: List[int]) -> None:
            if root is None:
                return
            if root.left is None and root.right is None:
                out.append(root.val)
                return
            collect(root.left, out)
            collect(root.right, out)

        seq1, seq2 = [], []
        collect(root1, seq1)
        collect(root2, seq2)
        return seq1 == seq2
