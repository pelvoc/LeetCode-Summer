class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        n=len(prices)
        if n<=1: return 0
        
        if k>=n/2:
            maxProfit=0
            for i in range(1, n): 
                if prices[i]>prices[i-1]: 
                    maxProfit+=(prices[i]-prices[i-1])
            return maxProfit
                    
        dp = [[0]*n for _ in range(k+2)]  
        for i in range(1, k+1):
            localMax=dp[i-1][0]-prices[0]
            for j in range(1, n): 
                dp[i][j]=max(dp[i][j-1], prices[j]+localMax)
                localMax=max(localMax, dp[i-1][j]-prices[j])

        return dp[k][n-1]