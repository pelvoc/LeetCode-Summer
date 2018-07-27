class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        leng=1
        count=9
        start=1
    
        while n>leng*count:
            n-=leng*count
            leng+=1
            count*=10
            start*=10
            
        start+=(n-1)/leng
        s=str(start)
        
        return int(s[(n-1)%leng])