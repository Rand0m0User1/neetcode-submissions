class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = dict()
        
        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in word_dict:
                word_dict[sorted_word] = [word]
            else: 
                word_dict[sorted_word].append(word)
            
        output = []

        for key in word_dict:
            output.append(word_dict[key])

        return output