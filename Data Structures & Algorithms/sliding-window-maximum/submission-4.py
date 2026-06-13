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

        '''
        i = 0
        max_heap = [(-1, 0)]
        0 < 0 - 4

        i = 1
        max_heap = [(-2, 1), (-1, 0)]
        1 < 1 - 4

        i = 2
        max_heap = [(-2, 1), (-1, 0), (-1, 0)]
        1 < 2 - 4
        2 == 2
        output = [2]

        i = 3
        max_heap = [(-2, 1), (-1, 0), (-1, 2), (0, 3)]
        1 < 3 - 4
        3 >= 2
        output = [2, 2]

        i = 4
        max_heap = [(-4, 4), (-2, 1), (-1, 0), (-1, 2), (0, 3)]
        4 < 4 - 4
        '''



