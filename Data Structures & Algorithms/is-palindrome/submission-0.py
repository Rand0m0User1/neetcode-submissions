class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars_in_string = [char.lower() for char in s if char.isalnum()]

        regular_string = ""
        for c in chars_in_string:
            regular_string += c

        reversed_string = ""
        for c in reversed(chars_in_string):
            reversed_string += c

        if reversed_string == regular_string:
            return True
        
        return False