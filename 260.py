class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dif=0
        for i in nums: 
            dif^=i
        dif&=-dif
        
        rets=[0, 0]
    
        for i in nums:
            if (i&dif)==0:
                rets[0]^=i
            else: 
                rets[1]^=i
                
        return rets