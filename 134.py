class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        r=len(gas)-1
        l=0
        sums=gas[r]-cost[r]
        
        while r>l:
            if sums>=0: 
                sums+=gas[l]-cost[l]       
                l+=1
            else: 
                r-=1
                sums+=gas[r]-cost[r]
        
        return r if sums>=0 else -1