class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        citations.sort()
        for i in range(l):
            if (l - i) <= citations[i]:
                return l - i
        return 0