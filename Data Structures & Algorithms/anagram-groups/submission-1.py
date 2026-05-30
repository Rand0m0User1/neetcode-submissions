from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        
        for word in strs:
            letter_frequencies = [0] * 26

            for char in word:
                letter_frequencies[ord(char) - ord('a')] += 1

            word_dict[tuple(letter_frequencies)].append(word)
            
        return list(word_dict.values())