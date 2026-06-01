class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums_set = set()
        longest_sequence = 0

        for i in range(len(nums)):
            nums_set.add(nums[i])

        for n in nums_set:
            if n-1 not in nums_set:
                current_num = n
                current_seq_length = 1

                while (current_num + 1) in nums_set:
                    current_num +=1
                    current_seq_length +=1

                longest_sequence = max(longest_sequence, current_seq_length)
        
        return longest_sequence