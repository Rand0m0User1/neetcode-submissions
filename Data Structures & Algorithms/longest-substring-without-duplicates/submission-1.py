class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right = 0, 1
        letters_found = set()
        longest = 0
        
        for right in range(len(s)):

            while s[right] in letters_found:
                letters_found.remove(s[left])
                left += 1
            
            letters_found.add(s[right])

            current_window_size = right - left + 1
            longest = max(longest, current_window_size)
        
        return longest