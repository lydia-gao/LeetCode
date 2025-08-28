from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': "abc", '3': "def",
            '4': "ghi", '5': "jkl", '6': "mno",
            '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        res: List[str] = []
        path: List[str] = []

        def dfs(pos: int) -> None:
            if pos == len(digits):
                res.append(''.join(path))
                return
            for ch in phone[digits[pos]]:
                path.append(ch)
                dfs(pos + 1)
                path.pop()

        dfs(0)
        return res
