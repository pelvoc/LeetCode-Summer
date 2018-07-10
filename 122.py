class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        profit = 0
        for i in range(1, n):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1] 
                
        return profit