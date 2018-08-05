class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m=len(matrix)
        if m==0: return 0
        n=len(matrix[0])
        
        maxA=0
        left=[0]*n
        right=[0]*n
        height=[0]*n
        
        for i in range(m): 
            curLeft=0 
            curRight=n
            for j in range(n):
                if matrix[i][j]=='1': 
                    height[j]+=1
                else: 
                    height[j]=0
            for j in range(n): 
                if matrix[i][j]=='1':
                    left[j]=max(left[j], curLeft)
                else: 
                    left[j]=0
                    curLeft=j+1
            for j in range(n-1, -1, -1):
                if matrix[i][j]=='1':
                    right[j]=min(right[j], curRight)
                else: 
                    right[j]=n
                    curRight=j
            for j in range(n):
                maxA=max(maxA, (right[j]-left[j])*height[j])
        
        return maxA