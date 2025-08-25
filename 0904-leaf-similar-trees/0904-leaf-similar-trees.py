# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root: Optional[TreeNode]):
            if root is None:
                return
            if root.left is None and root.right is None:
                yield root.val
            else:
                yield from leaves(root.left)
                yield from leaves(root.right)

        return list(leaves(root1)) == list(leaves(root2))
