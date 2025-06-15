from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        dic1 = Counter(word1)
        dic2 = Counter(word2)
        if set(dic1) != set(dic2):
            return False
        vals1 = Counter(dic1.values())
        vals2 = Counter(dic2.values())
        if vals1 != vals2:
            return False

        return True