class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, used, list, res):
            if len(list) == len(nums):
                res.append(list)
                return
    
            for i in range(0, len(nums)):
                if used[i]: continue
                if i>0 and nums[i-1]==nums[i] and not (used[i-1]): continue
                used[i]=True 
                list.append(nums[i])
                dfs(nums, used, list, res)
                used[i]=False
                list.remove(len(list)-1)
        
        res = []
        if nums==None or len(nums)==0: return res
        used = [False] * len(nums)
        list = [] 
        sorted(nums)
        dfs(nums, used, list, res)
        return res 
