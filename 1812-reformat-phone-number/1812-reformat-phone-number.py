class Solution:
    def reformatNumber(self, number: str) -> str:
        digit = [c for c in number if c.isdigit()]
        l = len(digit)
        res = []
        curr = 0
        while (l - curr) > 4:
            res.append(''.join(digit[curr:curr+3]))
            curr = curr + 3
        if l - curr == 4:
            res.append(''.join(digit[curr:curr + 2]))
            res.append(''.join(digit[curr+2:]))
        else:
            res.append(''.join(digit[curr:]))

        return '-'.join(res)