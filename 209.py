class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return 0
        
        i=0
        j=0
        minVal=sys.maxint
        sums=0
        
        while j<len(nums):
            sums+=nums[j]
            j+=1
            while sums>=s: 
                minVal=min(minVal, j-i)
                sums-=nums[i]
                i+=1
            
        return 0 if minVal==sys.maxint else minVal  