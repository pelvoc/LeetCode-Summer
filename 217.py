class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d=dict()
        
        for i in range(len(nums)):
            if nums[i] in d: 
                return True
            
            d[nums[i]]=nums[i]
            
        return False