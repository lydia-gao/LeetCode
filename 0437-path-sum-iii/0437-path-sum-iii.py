# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        # 以当前 node 为起点，沿着向下所有路径里，和为 targetSum 的条数
        def startsum(node: Optional[TreeNode], acc: int) -> int:
            if node is None:
                return 0
            curr = acc + node.val
            good = 1 if curr == targetSum else 0
            return good + startsum(node.left, curr) + startsum(node.right, curr)

        if root is None:
            return 0

        # 三部分之和：以 root 为起点的路径数 + 左子树所有起点 + 右子树所有起点
        return (startsum(root, 0)
                + self.pathSum(root.left, targetSum)
                + self.pathSum(root.right, targetSum))
