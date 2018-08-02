class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1=len(s1)
        l2=len(s2)
        
        if l1>l2: return False
        
        count=[0]*26
        
        for i in range(l1):
            count[ord(s1[i])-ord('a')]+=1
            count[ord(s2[i])-ord('a')]-=1
            
        if self.allZero(count):
            return True 
    
        for i in range(l1, l2):
            count[ord(s2[i])-ord('a')]-=1
            count[ord(s2[i-l1])-ord('a')]+=1
            if self.allZero(count): 
                return True
            
        return False

    def allZero(self, count):
        
        for i in range(26):
            if count[i]!=0: 
                return False
            return True
        