from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        if not root:
            return 0

        max_level = 1
        max_total = root.val
        curr = 1
        total = 0

        q1 = deque([root])
        q2 = deque()

        while q1:
            top = q1.popleft()
            total += top.val

            if top.left:
                q2.append(top.left)
            if top.right:
                q2.append(top.right)

            # End of current level
            if not q1:
                if total > max_total:
                    max_total = total
                    max_level = curr

                # Prepare for next level
                q1 = q2
                q2 = deque()
                total = 0
                curr += 1

        return max_level
