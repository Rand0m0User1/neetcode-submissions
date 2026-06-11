class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_counts = {}
        left = 0
        output = 0
        max_freq = 0

        for right in range(len(s)):
            char = s[right]
            letter_counts[char] = letter_counts.get(char, 0) + 1
            
            max_freq = max(max_freq, letter_counts[char])
            total_count = right - left + 1

            replacements = total_count - max_freq
            if replacements <= k:
                output = max(total_count, output)
            else:
                outgoing = s[left]
                letter_counts[outgoing] -= 1
                
                if letter_counts[outgoing] == 0:
                    del letter_counts[outgoing]

                left += 1

        return output