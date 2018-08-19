class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        res=[]
        if len(words)==0:
            return res
        
        d=dict()
        
        for w in words:
            d[w]=d.get(w, 0)+1
    
    
        dSorted=[(j, d[j]) for j in sorted(d, key=d.get, reverse=True)]    
        for i in range(k): 
            res.append(dSorted[i][0])
    
        return res