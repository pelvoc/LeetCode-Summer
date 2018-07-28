class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans=[]
        if len(digits)==0: return ans
        
        mapping=["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        ans.append('')

        for i in range(len(digits)):
            tmp=[]
            chars=mapping[ord(digits[i])-ord('0')]
            
            for c in range(len(chars)):
                for j in range(len(ans)): 
                    tmp.append(ans[j]+chars[c])
            ans=tmp
            
        return ans