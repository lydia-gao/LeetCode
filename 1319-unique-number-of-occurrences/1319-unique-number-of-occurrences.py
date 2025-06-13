from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = Counter(arr)
        s = set()
        for val in dic.values():
            if val not in s:
                s.add(val)
            else:
                return False
        return True