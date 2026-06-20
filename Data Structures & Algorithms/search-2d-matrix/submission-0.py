class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  
        if not matrix or not matrix[0]:
            return False

        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            
            row_middle = (top + bot) // 2

            if target < matrix[row_middle][0]:
                bot = row_middle - 1
            elif target > matrix[row_middle][-1]:
                top = row_middle + 1
            else:
                break
        else:
            return False
        
        return self.binarySearch(matrix[row_middle], target) != -1

    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2
            # left + (right - left) // 2

            current = nums[middle]

            if current == target:
                return middle
            elif current > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1