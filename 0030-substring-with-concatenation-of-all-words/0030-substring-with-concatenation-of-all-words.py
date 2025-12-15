from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        res = []

        for offset in range(word_len):
            left = offset
            right = offset
            curr = Counter()
            matched = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    curr[word] += 1
                    matched += 1

                    while curr[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        matched -= 1
                        left += word_len

                    if matched == num_words:
                        res.append(left)
                else:
                    curr.clear()
                    matched = 0
                    left = right

        return res
