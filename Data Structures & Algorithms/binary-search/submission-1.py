class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = left + (right - left) // 2

            current = nums[middle]

            if current == target:
                return middle
            elif current < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1