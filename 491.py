import copy

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.DFS([], 0, nums, res)
        
        return res
    
    def DFS(self, ls, index, nums, res):
    
        if len(ls)>1: 
            res.append(copy.copy(ls))
    
        used=set()
        
        for i in range(index, len(nums)):
            if nums[i] in used:
                continue
            if len(ls)==0 or nums[i]>=ls[len(ls)-1]:
                used.add(nums[i])
                ls.append(nums[i])
                self.DFS(ls, i+1, nums, res)
                ls.remove(ls[len(ls)-1])
    