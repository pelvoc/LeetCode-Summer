class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        res=[]
        d=dict()
        
        for s in strings:
            
            offset=ord(s[0])-ord('a')
            key=''
            
            for i in range(len(s)):
                c=ord(s[i])-offset
                if c< ord('a'):
                    c+=26
                key+=chr(c)
            
            if not (key in d):
                d[key]=[]
                
            d[key].append(s)
        
        # print d
        
        for key in d.keys(): 
            ls=d[key]
            ls=sorted(ls)
            res.append(ls)

        return res