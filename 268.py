class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l=len(nums)
        
        sums=l*(l+1)/2
        
        for n in nums:
            sums-=n
            
        return sums