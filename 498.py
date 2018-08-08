class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==None or len(matrix)==0: 
            return []
        m=len(matrix)
        n=len(matrix[0])
        res=[0]*(m*n)
        
        r=0
        c=0
        d=0
        dirs=[[-1, 1], [1, -1]]
        
        for i in range(m*n):
            res[i]=matrix[r][c]
            r+=dirs[d][0]
            c+=dirs[d][1]
        
            if r>=m: 
                r=m-1
                c+=2
                d=1-d
            if c>=n:
                c=n-1
                r+=2
                d=1-d
            if r<0:
                r=0
                d=1-d
            if c<0: 
                c=0
                d=1-d
            
        return res