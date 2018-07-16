class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # dict.get(key, default = None)
        sums, res=0,0
        preSum=dict()
        preSum[0]=1
    
        for i in range(len(nums)):
            sums+=nums[i]
            if (sums-k) in preSum: 
                res+=preSum[sums-k]
            preSum[sums]=preSum.get(sums, 0)+1
        
        return res