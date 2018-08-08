class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d=dict()
        runningSum=0
        
        for i in range(len(nums)): 
            runningSum+=nums[i]
            if k!=0: 
                runningSum%=k
            prev=d.get(runningSum)
            if prev!=None: 
                if (i-prev)>1: 
                    return True
            else: 
                d[runningSum]=i
        
        return False