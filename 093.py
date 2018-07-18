class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sl=len(s)
        res=[]
        i=1
        
        def isValid(s): 
            if len(s)>3 or len(s)==0 or (s[0]=='0' and len(s)>1) or int(s)>255: 
                return False
            return True
        
        while i<4 and i<sl-2: 
            j=i+1
            while j<i+4 and j<sl-1:
                k=j+1
                while k<j+4 and k<sl:
                    s1=s[0:i]
                    s2=s[i:j]
                    s3=s[j:k]
                    s4=s[k:sl]
                    if isValid(s1) and isValid(s2) and isValid(s3) and isValid(s4):
                        res.append(s1+"."+s2+"."+s3+"."+s4)
                    k+=1
                j+=1
            i+=1
            
    
        return res
        