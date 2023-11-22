## Space: O(1)
## Time: O(n)

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        ## Two pointer version
        if sorted(prices, reverse = True) == prices: ## if decreasing order, no profit can be made
            return 0
        
        elif sorted(prices) == prices: # if increasing order, maxc profit is the purchase on the first day and sell on the last day
            return prices[-1] - prices[0]
        
        else:
            max_profit = 0

            i, j = 0, 1
            while j < len(prices):
                if prices[i] < prices[j]:
                    profit = prices[j] - prices[i]
                    max_profit = max(max_profit, profit)
                else:
                    i = j ## shift left pointer all the way to the next low
                j += 1
    

        return max_profit
