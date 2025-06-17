class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for num in asteroids:
            while s != [] and (s[-1] > 0 and num < 0):
                if s[-1] + num == 0:
                    s.pop()
                    break
                if s[-1] > abs(num):
                    break
                s.pop()
            else:
                s.append(num)

        return s