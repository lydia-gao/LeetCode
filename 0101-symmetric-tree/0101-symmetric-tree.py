# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def is_symmetric(left: Optional[TreeNode], right: Optional[TreeNode]):
            if not left and not right:
                return True
            elif left and right:
                if left.val == right.val:
                    return is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)
            return False
        
        return is_symmetric(root.left, root.right)


        