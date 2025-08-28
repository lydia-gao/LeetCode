class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': "abc", '3': "def",
            '4': "ghi", '5': "jkl", '6': "mno",
            '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        s = [phone[d] for d in digits] 
        letter = []
        res = []

        def recur(i: int):
            if i == len(digits):
                res.append("".join(letter))
                return

            for char in s[i]:
                letter.append(char)
                recur(i + 1)
                letter.pop()
        
        recur(0)

        return res
        