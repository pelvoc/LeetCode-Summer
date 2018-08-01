class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l=len(citations)
        
        if l==0: return 0
            
        arr=[0]*(l+1)    
        
        for i in range(l): 
            if citations[i]>l:
                arr[l]+=1
            else: 
                arr[citations[i]]+=1
        
        t=0
        res=0
        
        for i in range(l, -1, -1): 
            t+=arr[i]
            if t>=i: 
                return i
        
        return 0