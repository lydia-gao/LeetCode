# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.res = 0

        def longest_zig(node):
            if not node:
                return (-1, -1)  
            left = 1 + longest_zig(node.left)[1]
            right = 1 + longest_zig(node.right)[0]
            self.res = max(left, right, self.res)
            return(left, right)
        
        longest_zig(root)
        return self.res