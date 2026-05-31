class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = []
        post = []
        
        product = 1
        for num in nums:
            pre.append(product)
            product *= num

        product = 1
        for num in reversed(nums):
            post.append(product)
            product *= num

        output = []

        count = len(nums) - 1
        for i in range(len(nums)):
            output.append(pre[i] * post[count])
            count -= 1

        return output