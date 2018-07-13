class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=-1
        for i in range(len(nums)-2, -1, -1): 
            if nums[i]<nums[i+1]:
                l=i
                break 
        
        if l==-1:
            return nums.reverse()
            
        r=-1
        for j in range(len(nums)-1, -1, -1): 
            if j>l and nums[j]>nums[l]: 
                r=j
                break
        
        nums[l], nums[r] = nums[r], nums[l]
        
        nums[l+1:]=reversed(nums[l+1:])