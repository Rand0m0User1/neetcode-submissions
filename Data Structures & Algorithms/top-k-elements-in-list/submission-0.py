class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_freqs = defaultdict(int)

        for num in nums:
            num_freqs[num] += 1

        sorted_vals = sorted(num_freqs.items(), key=lambda item: item[1], reverse=True)

        output = []

        for i in range(k):
            output.append(sorted_vals[i][0])

        return output