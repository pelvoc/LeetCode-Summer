class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if len(s)>len(t):
            return self.findTheDifference(t, s)
        
        #t longer than s
        d=[0]*26
        
        for si in s: 
            d[ord(si)-ord('a')]+=1
            
        for ti in t: 
            d[ord(ti)-ord('a')]-=1
        
        for i in range(len(d)):
            if d[i]<0: 
                return chr(i+ord('a'))