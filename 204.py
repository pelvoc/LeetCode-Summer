class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        notPrime=[False]*n
        
        count=0
        
        for i in range(2, n): 
            if notPrime[i]==False: 
                count+=1
                j=2
                while i*j<n: 
                    notPrime[i*j]=True
                    j+=1
                
        return count