class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return s
        
        res=list(s)
        
        l=0
        r=len(s)-1
        
        d='aeiouAEIOU'

        while l<r:
            
            while l<r and not(res[l] in d):
                l+=1
    
            while l<r and not(res[r] in d):
                r-=1            
                
            res[l], res[r] = res[r], res[l]
            
            l+=1
            r-=1
            
        
        return ''.join(res)