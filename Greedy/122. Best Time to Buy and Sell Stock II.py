# Solution
# Runtime: 52 ms, faster than 97.56% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 15 MB, less than 89.33% of Python3 online submissions for Best Time to Buy and Sell Stock II.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 1:
            return 0
        
        
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                profit += prices[i] - prices[i-1]
                
        return profit