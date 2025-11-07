class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zig = [""] * numRows
        isup = False
        zig[0] = s[0]
        idx = 1
        for l in s[1:]:
            zig[idx] += l
            if idx == numRows - 1 or idx == 0:
                isup = not isup
            if isup:
                idx -= 1
            else:
                idx += 1
        return "".join(zig)