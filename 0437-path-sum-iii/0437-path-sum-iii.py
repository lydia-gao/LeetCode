class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_from(node: Optional[TreeNode], remain: int) -> int:
            if not node:
                return 0
            cnt = 1 if node.val == remain else 0
            cnt += count_from(node.left, remain - node.val)
            cnt += count_from(node.right, remain - node.val)
            return cnt

        if not root:
            return 0
        return (count_from(root, targetSum)
                + self.pathSum(root.left, targetSum)
                + self.pathSum(root.right, targetSum))
