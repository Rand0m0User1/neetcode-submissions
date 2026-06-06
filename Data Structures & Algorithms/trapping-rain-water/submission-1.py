class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        output = 0
        
        while left < right:

            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                left += 1
            elif height[left] > height[right]:
                right_max = max(right_max, height[right])
                right -= 1

            if left_max > height[left]:
                output += left_max - height[left]
            
            if right_max > height[right]:
                output += right_max - height[right]

        return output