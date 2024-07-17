class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowers_placed = 0
        if n == 0:
            return True
        if len(flowerbed) < n:
            return False
        if len(flowerbed) == 1 and flowerbed[0] == 1:
            return False
        elif len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        for i in range(len(flowerbed)):
            if i != 0 and i != len(flowerbed) - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    flowers_placed += 1
            else:
                if i == 0:
                    if flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                        flowerbed[i] = 1
                        flowers_placed += 1
                else:
                    if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                        flowerbed[i] = 1
                        flowers_placed += 1
        if flowers_placed >= n:
            return True
        else:
            return False
