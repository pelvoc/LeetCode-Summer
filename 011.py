class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        w=0
    
        l=0
        r=len(height)-1
        
        while l<r:
            h=min(height[l], height[r])
            w=max(w, (r-l)*h)
            
            while height[l]<=h and l<r: 
                l+=1
            while height[r]<=h and l<r: 
                r-=1
            
        return w
        