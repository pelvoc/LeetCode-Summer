class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        r=len(ratings)
        
        if r<=1: return r
    
        num=[1]*r
        
        for i in range(1, r):
            if ratings[i]>ratings[i-1]:
                num[i]=num[i-1]+1
            
        for i in range(r-1, 0, -1):
            if ratings[i-1]>ratings[i]:
                num[i-1]=max(num[i]+1, num[i-1])
                
        res=0
        for i in range(r):
            res+=num[i]
            
        return res