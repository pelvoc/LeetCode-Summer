class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        island=0
        nei=0
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]==1:
                    island+=1
                    if r+1<len(grid) and grid[r+1][c]==1: 
                        nei+=1
                    if c+1<len(grid[r]) and grid[r][c+1]==1: 
                        nei+=1
                
        return island*4-nei*2