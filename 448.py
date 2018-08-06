class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        n=len(nums)
        for i in range(n):
            val=abs(nums[i])-1
            if nums[val]>0: 
                nums[val]=-nums[val]
            
        for i in range(n):
            if nums[i]>0: 
                res.append(i+1)
                
        return res