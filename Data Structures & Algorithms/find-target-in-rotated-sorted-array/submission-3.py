class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:

            middle = (left + right) // 2
            print(f"mid: {middle}")

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        if target == nums[left]:
            return left
        elif target >= nums[left] and target <= nums[-1]:
            return self.binarySearch(nums, left, len(nums) - 1, target)
        else:
            return self.binarySearch(nums, 0, left - 1, target)

    
    def binarySearch(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            
            middle = (right + left) // 2

            current = nums[middle]

            if current == target:
                return middle
            elif current > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1