# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        found = False
        def count(root):
            if not root:
                return 0
            return root.val + count(root.left) + count(root.right)
        total = count(root)
        if total % 2 != 0:
            return False
        def dfs(root):
            nonlocal found
            if not root:
                return 0
            if found:
                return 0
            acc = root.val + dfs(root.left) + dfs(root.right)
            if acc == total // 2:
                found = True
            return acc
        dfs(root.left)
        dfs(root.right)
        return found