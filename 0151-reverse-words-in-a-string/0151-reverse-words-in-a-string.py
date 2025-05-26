class Solution:
    def reverseWords(self, s: str) -> str:
        i = len(s) - 1
        res = []

        while i >= 0:
            # 跳过空格
            if s[i] == ' ':
                i -= 1
                continue

            # 找到当前单词的末尾
            end = i
            # 向前找到单词的开头
            while i >= 0 and s[i] != ' ':
                i -= 1
            start = i + 1
            res.append(s[start:end+1])

        return ' '.join(res)
