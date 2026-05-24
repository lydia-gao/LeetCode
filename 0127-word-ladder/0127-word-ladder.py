from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque()
        q.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        letters = "abcdefghijklmnopqrstuvwxyz"

        while q:
            curr, count = q.popleft()

            if curr == endWord:
                return count

            for i in range(len(curr)):
                for ch in letters:
                    new_word = curr[:i] + ch + curr[i + 1:]

                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word, count + 1))

        return 0