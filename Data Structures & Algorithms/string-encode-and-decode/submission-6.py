class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if strs == []:
            return "▲"

        complete_string = "•".join(strs)
        
        return complete_string

    def decode(self, s: str) -> List[str]:

        if "▲" in s:
            return []

        words_list = s.split("•")

        return words_list