class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if s==0: return 0
        
        memo=[0]*(n+1)
        memo[n]=1
        
        if s[n-1]!='0':
            memo[n-1]=1
        else: 
            memo[n-1]=0
        
        for i in range(n-2, -1, -1):
            if s[i]=='0': 
                continue
            else: 
                if int(s[i:i+2])<=26: 
                    memo[i]=memo[i+1]+memo[i+2]
                else: 
                    memo[i]=memo[i+1]
        
        return memo[0]