class TimeMap:

    def __init__(self):
        self.store = {}
        self.timestamp_prev = 0
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append([timestamp, value])

    # key1: [[10, "value1"]]

    # get key1, 1

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        left = 0
        right = len(self.store[key]) - 1
        result = ""

        while left <= right:
            middle = (left + right) // 2
            current = self.store[key][middle]

            if current[0] == timestamp:
                return current[1]
            elif current[0] < timestamp:
                result = current[1]
                left = middle + 1
            else:
                right = middle - 1

        return result
