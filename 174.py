class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m=len(dungeon)
        n=len(dungeon[0])
        
        hp=[[sys.maxint]*(n+1) for _ in range(m+1)]
        
        hp[m][n-1]=1
        hp[m-1][n]=1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                need=min(hp[i+1][j], hp[i][j+1])-dungeon[i][j]
                
                hp[i][j]= 1 if need<=0 else need
        
        return hp[0][0]