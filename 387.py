class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt=[0]*26
        
        for i in range(len(s)):
            cnt[ord(s[i])-ord('a')]+=1
            
        for i in range(len(s)):
            if cnt[ord(s[i])-ord('a')]==1: 
                return i
            
        return -1