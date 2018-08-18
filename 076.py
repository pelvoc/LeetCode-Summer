class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls=[0]*128
        
        for c in t: 
            ls[ord(c)-ord('A')]+=1
        
        # print ls 
        counter=len(t)
        begin=0
        end=0
        d=sys.maxint
        head=0
        
        while end<len(s):
            
            # print ord(s[end])-ord('A')
            if ls[ord(s[end])-ord('A')]>0: 
                counter-=1
            ls[ord(s[end])-ord('A')]-=1
            end+=1
                
            while counter==0: 
                if end-begin<d: 
                    head=begin
                    d=end-begin
                    
                
                if ls[ord(s[begin])-ord('A')]==0: 
                    counter+=1
                ls[ord(s[begin])-ord('A')]+=1
                begin+=1
                    
        
        return '' if d==sys.maxint else s[head:d]