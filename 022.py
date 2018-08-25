class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ls=[]
        self.backtrack(ls, '', 0, 0, n)
        
        return ls
        
    def backtrack(self, ls, s, left, right, maxVal):
        
        if len(s)==2*maxVal: 
            ls.append(s)
            return 
        
        if left<maxVal: 
            self.backtrack(ls, s+"(", left+1, right, maxVal)
        if right<left:
            self.backtrack(ls, s+")", left, right+1, maxVal)