class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        r=len(s)-1
        
        while l<r: 
            if s[l]!=s[r]:
                return self.isPalindromic(s, l, r+1) or self.isPalindromic(s, l-1, r)
            
            l+=1
            r-=1
        
        return True
    
    def isPalindromic(self, s, l, r):
        
        l+=1
        r-=1
        
        while l<r: 
            
            if s[l]!=s[r]:
                return False
    
            l+=1
            r-=1
    
        return True