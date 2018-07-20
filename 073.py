class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0=1
        cols=len(matrix[0])
        rows=len(matrix)
        
        for i in range(0, rows): 
            if matrix[i][0]==0: 
                col0=0
            for  j in range(1, cols):
                if matrix[i][j]==0:
                    matrix[i][0]=matrix[0][j]=0
        
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, 0, -1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if col0==0: 
                matrix[i][0]=0 