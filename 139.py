class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        tmpString=[]
        for char in s: 
            
            tmpString+=char
            if tmpString in wordDict:
                tmpString=[]
                continue
                
        f=[False]*(len(s)+1)
        f[0]=True
        
        for i in range(1, len(s)+1): 
            for d in wordDict: 
                if len(d)<=i:
                    if f[i-len(d)]:
                        if s[i-len(d):i]==d:
                            f[i]=True
                            break

        for i in range(1, len(s)+1):
            for j in range(0, i):
                if f[j] and s[j:i] in wordDict: 
                    f[i]=True
                    break
        
        return f[len(s)]