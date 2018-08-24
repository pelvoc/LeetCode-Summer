class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sb=[]
        carry=0
        # for i in zip(range(len(num1), -1, -1), range(len(num2), -1, -1)): 
        i=len(num1)-1
        j=len(num2)-1
        while i>=0 or j>=0 or carry==1: 
            x=0 if i<0 else ord(num1[i])-ord('0')
            y=0 if j<0 else ord(num2[j])-ord('0')
            sb.append(str((x+y+carry)%10))
            carry=(x+y+carry)/10
            
            i-=1
            j-=1
            
        return ''.join(reversed(sb))