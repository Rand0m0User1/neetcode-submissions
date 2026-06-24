class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        largest_profit = 0

        while right < len(prices):
            
            if prices[left] < prices[right]:
                largest_profit = max((prices[right] - prices[left]), largest_profit)
            else:
                left = right

            right += 1

        return largest_profit
