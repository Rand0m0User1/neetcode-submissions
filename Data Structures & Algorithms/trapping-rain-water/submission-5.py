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
                output += left_max - height[left]
                left += 1
            elif height[left] > height[right]:
                right_max = max(right_max, height[right])
                output += right_max - height[right]
                right -= 1

        return output

        '''
        [0,2,0,3,1,0,1,3,2,1]

        left | right | l_idx | r_idx | l_max | r_max | output
        0      1       0       9       0       0       0    (Initial State)

        0  <   1       1       9       0       0       0    (Process idx 0: l_max becomes 0, water +0)
        2  >   1       1       8       2       0       0    (Process idx 9: r_max becomes 1, water +0)
        2  =   2       2       8       2       1       0    (Process idx 8: r_max becomes 2, water +0)
        0  <   2       3       8       2       2       2    (Process idx 2: water += 2 - 0 = +2)
        3  >   2       3       7       3       2       2    (Process idx 3: l_max becomes 3, water +0)
        3  =   3       4       7       3       3       2    (Process idx 7: r_max becomes 3, water +0)
        1  <   3       5       7       3       3       4    (Process idx 4: water += 3 - 1 = +2)
        0  <   3       6       7       3       3       7    (Process idx 5: water += 3 - 0 = +3)
        1  <   3       7       7       3       3       9    (Process idx 6: water += 3 - 1 = +2)
        '''