class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses=sorted(houses)
        heaters=sorted(heaters)
        
        i,j,res=0,0,0
        
        while i<len(houses):
            while j<len(heaters)-1 and abs(heaters[j+1]-houses[i]<=abs(heaters[j]-houses[i])): 
                j+=1
            res=max(res, abs(heaters[j]-houses[i]))
            i+=1
        
        return res