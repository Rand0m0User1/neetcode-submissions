class Solution:

    def __init__(self):
        self.seen = set()

    def isHappy(self, n: int) -> bool:

        if n == 1:
            return True
        
        if n in self.seen:
            return False 

        self.seen.add(n)

        digits = [int(n) for n in str(n)]

        sum = 0
        for i in range(len(digits)):
            sum += pow(digits[i], 2)
        
        return self.isHappy(sum)