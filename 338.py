class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        f=[0]*(num+1)
        
        for i in range(1,num+1): 
            f[i]=f[i>>1]+(i&1)
        return f