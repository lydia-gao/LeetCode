class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        prev_str = ""
        repeat = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                repeat = repeat * 10 + int(c)  # 支持多位数
            if c == "[":
                stack.append([prev_str, repeat])
                prev_str = ""
                repeat = 0
            if c.isalpha():
                prev_str += c
            if c == "]":
                info = stack.pop()
                prev_str = info[0] + info[1] * prev_str
        return prev_str
