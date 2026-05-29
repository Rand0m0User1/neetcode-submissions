class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_dict_s = dict()
        letter_dict_t = dict()

        if len(s) != len(t):
            return False

        for letter in s:
            if letter not in letter_dict_s:
                letter_dict_s[letter] = 1

            letter_dict_s[letter] += 1

        for letter in t:
            if letter not in letter_dict_t:
                letter_dict_t[letter] = 1

            letter_dict_t[letter] += 1

        return letter_dict_t == letter_dict_s