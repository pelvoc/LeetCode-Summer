class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        
        alphabet = [0] * 26
        
        for i in range(len(s)): 
            alphabet[ord(s[i])-ord('a')]+=1
        for j in range(len(t)): 
            alphabet[ord(t[j])-ord('a')]-=1
        for k in alphabet:
            if k!=0:
                return False
        return True  