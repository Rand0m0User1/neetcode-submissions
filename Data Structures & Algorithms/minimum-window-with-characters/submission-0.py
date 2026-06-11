class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_freqs = {}
        t_freqs = {}
        left = 0
        t_counts = len(set(t))
        substr_counts = 0
        output = ""

        for i in range(len(t)):
            t_char = t[i]
            t_freqs[t_char] = t_freqs.get(t_char, 0) + 1
        
        for right in range(len(s)):
            char = s[right]
            s_freqs[char] = s_freqs.get(char, 0) + 1

            if char in t_freqs and s_freqs[char] == t_freqs[char]:
                substr_counts += 1

            while t_counts == substr_counts:
                current_window = s[left : right + 1]
                if output == "" or len(current_window) < len(output):
                    output = current_window

                outgoing = s[left]
                s_freqs[outgoing] -= 1

                if outgoing in t_freqs and s_freqs[outgoing] < t_freqs[outgoing]:
                    substr_counts -= 1
            
                left += 1

        return output

