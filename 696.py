class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prevLen=0
        curLen=1
        res=0
        
        for i in range(1, len(s)):
            if s[i]==s[i-1]: 
                curLen+=1
            else:
                prevLen=curLen
                curLen=1
                
            if prevLen>=curLen: 
                res+=1

        return res