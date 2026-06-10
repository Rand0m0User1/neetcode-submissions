class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        s1_count = {}
        
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        window_count = {}
        for i in range(len(s1)):
            char = s2[i]
            window_count[char] = window_count.get(char, 0) + 1

        if window_count == s1_count:
            return True

        for right in range(len(s1), len(s2)):
            new_char = s2[right]
            window_count[new_char] = window_count.get(new_char, 0) + 1

            outgoing_char = s2[left]
            window_count[outgoing_char] -= 1

            if window_count[outgoing_char] == 0:
                del window_count[outgoing_char]

            left += 1
            
            if window_count == s1_count:
                return True

        return False