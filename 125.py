class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s==None: return True
        
        head=0
        tail=len(s)-1
        d="A-Za-z0-9"
        
        while head<=tail: 
            cHead=s[head]
            cTail=s[tail]
        
            if not (cHead.isdigit() or cHead.isalpha()): 
                head+=1
            elif not (cTail.isdigit() or cTail.isalpha()):
                tail-=1
            else: 
                if cHead.lower() != cTail.lower():
                    return False
                head+=1
                tail-=1
                
        return True