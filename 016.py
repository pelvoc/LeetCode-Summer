class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res=nums[0]+nums[1]+nums[len(nums)-1]
        
        for i in range(len(nums)-2):
            start=i+1
            end=len(nums)-1
            while start<end:
                sums=nums[i]+nums[start]+nums[end]
                if sums>target: 
                    end-=1
                elif sums<target:
                    start+=1
                else: 
                    start+=1
                    
                if abs(sums-target) < abs(res-target): 
                    res=sums
        
        return res