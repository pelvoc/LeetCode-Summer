class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sums=0
        for n in nums: 
            sums+=n
        
        return 0 if sums<S or (S+sums)%2>0 else self.subsetSum(nums, (S+sums)>>1)
        
    def subsetSum(self, nums, S): 
        dp=[0]*(S+1)
        dp[0]=1
        for n in nums:
            for i in range(S, n-1, -1):
                dp[i]+=dp[i-n]
        return dp[S]