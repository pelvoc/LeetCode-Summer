import Queue as queue


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(matrix)
        n=len(matrix[0])
        
        q=queue.Queue()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    q.put([i,j])
                else:
                    matrix[i][j]=sys.maxint
            
        dirs=[[-1,0],[1,0],[0,1],[0,-1]]
        
        while not q.empty(): 
            cell=q.get()
            for d in dirs:
                r=cell[0]+d[0]
                c=cell[1]+d[1]
                if r<0 or r>=m or c<0 or c>=n or matrix[r][c]<=matrix[cell[0]][cell[1]]+1:
                    continue
                q.put([r,c])
                matrix[r][c]=matrix[cell[0]][cell[1]]+1
            
        return matrix