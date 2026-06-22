import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            k = (left + right) // 2

            hours_spent = sum(math.ceil(pile / k) for pile in piles)

            if hours_spent <= h:
                right = k
            else:
                left = k + 1

        return left
        # piles=[30,11,23,4,20]
        # h=6
        
        