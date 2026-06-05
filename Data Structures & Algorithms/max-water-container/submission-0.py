class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        largest_area = 0

        while left < right:
            area = (right - left) * min(heights[right], heights[left])

            largest_area = max(largest_area, area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return largest_area

        