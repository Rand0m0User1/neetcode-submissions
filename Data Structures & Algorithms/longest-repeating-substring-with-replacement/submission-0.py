class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_counts = {}
        left = 0
        output = 0

        for right in range(len(s)):
            char = s[right]
            letter_counts[char] = letter_counts.get(char, 0) + 1
            
            total_count = sum(letter_counts.values())
            most_freq_letter = max(letter_counts.values())

            replacements = total_count - most_freq_letter
            if replacements <= k:
                output = max(most_freq_letter + replacements, output)
            else:
                outgoing = s[left]
                letter_counts[outgoing] = letter_counts.get(outgoing, 0) - 1
                
                if letter_counts[outgoing] == 0:
                    del letter_counts[outgoing]

                left += 1

        return output