from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        q = deque()
        res = []
        q.append(root)
        q.append(None)
        while q:
            top = q.popleft()
            if not top:
                continue                
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
            if q[0] == None:
                q.append(None)
                res.append(top.val)
        return res
            

        