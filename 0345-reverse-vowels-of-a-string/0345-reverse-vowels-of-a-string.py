class Solution:
    def reverseVowels(self, s: str) -> str:
        first = 0
        second = len(s) - 1
        new = list(s)
        vow = list('aeiouAEIOU')
        while (first < second) :
            if s[first] not in vow:
                first += 1
                continue
            if s[second] not in vow:
                second -= 1
                continue
            new[first] = s[second]
            new[second] = s[first]
            first += 1
            second -= 1
        return ''.join(new)
