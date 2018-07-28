class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=1:
            return False
        
        sums=0
        for num in nums:
            sums+=num
            
        if (sums%2)==1: #odd
            return False
        
        sums=sums/2
        
        n=len(nums)
        
        dp=[[False]*(sums+1) for _ in range(n+1)]
        
        # for i in range(len(dp)):
        #     dp[i][j]=0 for j in range(len(dp[i]))
        
        dp[0][0]=True
        
        for i in range(1, n+1):
            dp[i][0]=True
        for j in range(1, sums+1):
            dp[0][j]=False
        
        for i in range(1, n+1):
            for j in range(1, sums+1):
                dp[i][j]=dp[i-1][j]
                if j>=nums[i-1]:
                    dp[i][j]=(dp[i][j] or dp[i-1][j-nums[i-1]])
                
        return dp[n][sums]