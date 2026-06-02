class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        sums = []

        def dfs(node):
            if not node:
                return 0

            curr = node.val + dfs(node.left) + dfs(node.right)
            sums.append(curr)
            return curr

        total = dfs(root)

        # remove root's total sum because we cannot cut above root
        sums.pop()

        if total % 2 != 0:
            return False

        return total // 2 in sums