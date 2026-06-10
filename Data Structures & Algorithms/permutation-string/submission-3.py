class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        s1_count = {}
        
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        for right in range(len(s1), len(s2) + 1):
            window_count = {}
            window = s2[left:right]

            print(window)

            for char in window:
                window_count[char] = window_count.get(char, 0) + 1
            
            if window_count == s1_count:
                return True

            left += 1

        return False