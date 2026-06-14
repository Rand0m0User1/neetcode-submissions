class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in closing_mapping:
                top_element = stack.pop() if stack else "."
                
                if closing_mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0