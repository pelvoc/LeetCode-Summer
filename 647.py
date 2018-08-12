class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.count=0
        
        if s==None or len(s)==0: return 0
        
        for i in range(len(s)): 
            self.extendPalindrome(s, i, i); # odd length;
            self.extendPalindrome(s, i, i + 1); # even length
    
        return self.count
    
    def extendPalindrome(self, s, left, right):
        
        while left>=0 and right<len(s) and s[left]==s[right]: 
            self.count+=1
            left-=1
            right+=1
    