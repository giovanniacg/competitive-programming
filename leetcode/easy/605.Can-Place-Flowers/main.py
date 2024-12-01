from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        tam = len(flowerbed)
        if tam == 1:
            return True if flowerbed[0] else False

        for i in range(tam):
            if flowerbed[i] == 1:
                continue

            can_add = False

            if i != tam - 1:
                if flowerbed[i + 1] == 0:
                    can_add = True
            else:
                can_add = True

            if i != 0:
                if flowerbed[i - 1] == 0:
                    if can_add:
                        n -= 1
                        flowerbed[i] = 1
            else:
                if can_add:
                    n -= 1
                    flowerbed[i] = 1

            if n == 0:
                print(flowerbed)
                return True
        return False


n = int(input())

flowerbed = list(map(int, input().strip("[]").split(",")))

s = Solution()
s.canPlaceFlowers(flowerbed, n)
