import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        output = []

        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))

            while max_heap and max_heap[0][1] < i - k + 1:
                heapq.heappop(max_heap)

            if i >= k - 1:
                output.append(-max_heap[0][0])

        return output