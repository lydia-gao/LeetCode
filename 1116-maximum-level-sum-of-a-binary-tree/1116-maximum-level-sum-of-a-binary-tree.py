from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        max_level = 1
        max_total = root.val
        curr = 1
        
        q1 = deque([root])
        
        while q1:
            total = 0
            q2 = deque()
            while q1:
                top = q1.popleft()
                total += top.val
                if top.left:
                    q2.append(top.left)
                if top.right:
                    q2.append(top.right)
            
            if total > max_total:
                max_total = total
                max_level = curr
                
            q1 = q2
            curr += 1
        
        return max_level
