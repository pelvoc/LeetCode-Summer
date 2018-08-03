import copy

class Solution(object):
    
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        for i in range(len(input)):
            if input[i]=='-' or input[i]=='*' or input[i]=='+': 
                p1=input[0:i]
                p2=input[i+1:]
                
                p1ret=self.diffWaysToCompute(p1)
                p2ret=self.diffWaysToCompute(p2)
        
                for p1 in p1ret:
                    for p2 in p2ret: 
                        c=0
                        if input[i]=='+': 
                            c=p1+p2
                            break
                        elif input[i]=='-': 
                            c=p1-p2
                            break
                        elif input[i]=='-': 
                            c=p1*p2
                            break
                    res.append(copy.copy(c))
                    
        if len(res)==0: 
            res.append(copy.copy(int(input)))
            
        return res