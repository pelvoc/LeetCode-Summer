# sliding window

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res=[]
        if len(p)>len(s): return res
        d=dict()
        
        for c in p: 
            d[c]=d.get(c, 0)+1
        
        counter=len(d)
        
        begin=0
        end=0
        head=0
        leng=sys.maxint
        
        while end<len(s): 
            c=s[end]
            if d.get(c):
                d[c]=d.get(c)-1
                if d[c]==0: counter-=1
            end+=1
            while counter==0:
                tmpC=s[begin]
                if d.get(tmpC):
                    d[tmpC]=d.get(tmpC)+1
                    if d[tmpC]>0:
                        counter+=1
                if end-begin==len(p): 
                    res.append(begin)
                begin+=1
                
        return res
        