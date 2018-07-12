class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0: return 0
        
        maxL = 0
        j=0
        dic = dict()
        
        for i in range(len(s)):
            if s[i] in dic: 
                j = max(j, dic[s[i]]+1)
    
            dic[s[i]] = i 
            maxL = max(maxL, i-j+1)
    
        return maxL
        