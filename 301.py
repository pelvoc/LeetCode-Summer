import copy

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        self.remove(s, res, 0, 0, ['(', ')'])
        return res
    
    def remove(self, s, res, last_i, last_j, par): 
        
        stack=0
        for i in range(last_i, len(s)):
            if s[i]==par[0]:
                stack+=1
            if s[i]==par[1]:
                stack-=1
            if stack>=0:
                continue
            for j in range(last_j, i+1): 
                if s[j]==par[1] and (j==last_j or s[j-1]!=par[1]):
                    self.remove(s[0:j]+s[j+1:len(s)], res, i, j, par)
            return 

        reverse=copy.copy(s[::-1])
        if par[0]=='(': 
            self.remove(reverse, res, 0, 0, [')', '('])
        else: 
            res.append(reverse)