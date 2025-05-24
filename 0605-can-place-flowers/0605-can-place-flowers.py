class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spot = 0
        for i in range(len(flowerbed)):
            good = (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0) and flowerbed[i] == 0
            if good:
                flowerbed[i] = 1
                spot += 1
        return spot >= n