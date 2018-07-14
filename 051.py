class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        self.DFS([],[],[], n, result)
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]        
    def DFS(self, queens, xy_dif, xy_sum, n, result):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                self.DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q], n, result)