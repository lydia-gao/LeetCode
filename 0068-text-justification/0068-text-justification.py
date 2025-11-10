class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        res = []
        curr = []
        curr_len = 0

        for w in words:
            if curr_len + len(w) + len(curr) > maxWidth:  # len(curr) for spaces
                spaces = maxWidth - curr_len
                if len(curr) == 1:
                    res.append(curr[0] + ' ' * spaces)
                else:
                    space_between = spaces // (len(curr) - 1)
                    extra = spaces % (len(curr) - 1)
                    line = ''
                    for i in range(len(curr)):
                        line += curr[i]
                        if i < len(curr) - 1:
                            line += ' ' * (space_between + (1 if i < extra else 0))
                    res.append(line)
                curr = []
                curr_len = 0
            curr.append(w)
            curr_len += len(w)

        # last line: left justify
        last_line = ' '.join(curr)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)

        return res

