class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0: return 0
        if n==1: return 1
        if n==2: return 2
        
        oneStep=2
        twoStep=1
        allways=0
        
        for i in range(2, n):
            allways=oneStep+twoStep
            twoStep=oneStep
            oneStep=allways
        
        return allways