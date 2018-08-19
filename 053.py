class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[0]*n
        
        dp[0]=nums[0]
        maxs=dp[0]

        for i in range(1, n):
            if dp[i-1]>0: 
                dp[i]=nums[i] + dp[i-1] 
            else:
                dp[i]=nums[i] + 0 
            maxs=max(maxs, dp[i])
        
        return maxs