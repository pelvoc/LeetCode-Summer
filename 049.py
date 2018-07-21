class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)==0: return []
        
        d=dict()
        
        for s in strs:
            keyStr=''.join(sorted(s))
            if not (keyStr in d): 
                d[keyStr]=[]
            
            d[keyStr].append(s)
        
        return d.values()