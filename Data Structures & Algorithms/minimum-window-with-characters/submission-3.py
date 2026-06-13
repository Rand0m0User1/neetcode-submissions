class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_freqs = {}
        t_freqs = {}
        left = 0
        t_counts = len(set(t))
        substr_counts = 0
        
        min_len = float('inf')
        best_window_indices = (-1, -1)

        for i in range(len(t)):
            t_char = t[i]
            t_freqs[t_char] = t_freqs.get(t_char, 0) + 1
        
        for right in range(len(s)):
            char = s[right]
            s_freqs[char] = s_freqs.get(char, 0) + 1

            if char in t_freqs and s_freqs[char] == t_freqs[char]:
                substr_counts += 1

            while t_counts == substr_counts:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    best_window_indices = (left, right)

                outgoing = s[left]
                s_freqs[outgoing] -= 1

                if outgoing in t_freqs and s_freqs[outgoing] < t_freqs[outgoing]:
                    substr_counts -= 1
            
                left += 1

        start, end = best_window_indices
        return s[start : end + 1] if min_len != float('inf') else ""