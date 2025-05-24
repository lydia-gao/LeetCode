class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = []
        l1 = len(word1)
        l2 = len(word2)
        pos1 = 0
        pos2 = 0
        even = True

        while pos1 < l1 and pos2 < l2:
            if even:
                new.append(word1[pos1])
                pos1 += 1
            else:
                new.append(word2[pos2])
                pos2 += 1
            even = not even  # 切换交替状态

        # 拼接剩下的部分
        if pos1 < l1:
            new.extend(word1[pos1:])
        if pos2 < l2:
            new.extend(word2[pos2:])

        return ''.join(new)
