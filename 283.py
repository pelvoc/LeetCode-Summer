class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0: return []
        
        pos=0
        for n in nums: 
            if n!=0: 
                nums[pos]=n
                pos+=1
          
        for i in range(pos, len(nums)): 
            nums[i]=0