import json
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        return json.dumps(strs)

    def decode(self, s: str) -> List[str]:
        return json.loads(s)