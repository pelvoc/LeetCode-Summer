import math

class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        sb=''  #string builder
        total=math.pow(k,n)
        
        for i in range(n):
            sb+='0'
        
        visited=[]
        visited.append(sb)
        
        self.DFS(sb, total, visited, n, k)

        return sb
        
    def DFS(self, sb, goal, visited, n, k):
        if len(visited)==goal: 
            return True
        
        prev=sb[len(sb)-n+1:len(sb)]
        
        for i in range(k):
            then=prev+chr(i)
            if not (then in visited): 
                visited.append(then)
                sb+=chr(i)
                if self.DFS(sb, goal, visited, n, k):
                    return True
                else: 
                    visited.remove(then)
                    sb=sb[:-2]
        
        return False