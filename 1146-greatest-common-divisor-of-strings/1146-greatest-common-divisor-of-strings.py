class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_len = min(len(str1), len(str2))

        for com in range(min_len, 0, -1):
            comword = str1[:com]
            if len(str1) % com == 0 and len(str2) % com == 0:
                if comword * (len(str1) // com) == str1 and comword * (len(str2) // com) == str2:
                    return comword
        return ""