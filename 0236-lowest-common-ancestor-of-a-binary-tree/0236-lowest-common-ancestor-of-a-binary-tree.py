# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if not node:
                return (None, False, False)

            left_lca, left_p, left_q = dfs(node.left)
            right_lca, right_p, right_q = dfs(node.right)

            found_p = left_p or right_p or node is p
            found_q = left_q or right_q or node is q

            # If LCA already found in left or right subtree, return it
            if left_lca:
                return (left_lca, True, True)
            if right_lca:
                return (right_lca, True, True)

            # If current node is the split point
            if found_p and found_q:
                return (node, True, True)

            return (None, found_p, found_q)

        lca, _, _ = dfs(root)
        return lca