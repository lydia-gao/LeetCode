class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # l = len(citations)
        # citations.sort()
        # for i in range(l):
        #     if (l - i) <= citations[i]:
        #         return l - i
        # return 0
        n = len(citations)
        count = [0] * (n + 1)
        for c in citations:
            count[min(n, c)] += 1
        acc = 0
        for i in range(n, -1, -1):
            acc += count[i]
            if i <= acc:
                return i
        return 0