class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        d=dict()
        for i in range(len(nums)):
            if (target-nums[i]) in d: 
                res.append(i)
                res.append(d[target-nums[i]])
                return res
            d[nums[i]]=i
        
        return res
        