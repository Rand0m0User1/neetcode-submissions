class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}

        for word in strs:
            freqs = [0] * 26

            for character in word:
                freqs[ord(character) - ord('a')] += 1

            key = tuple(freqs)

            if key not in word_dict:
                word_dict[key] = []

            word_dict[key].append(word)
        
        return list(word_dict.values())
            
