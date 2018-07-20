class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        base = 0
        i = 0
        
        while str[i]==' ': 
            i+=1
        if str[i] == '-' or str[i] == '+':  
            sign = 1 - 2 * (str[i] == '-')
            i+=1
        
        while str[i] >= '0' and str[i] <= '9': 
            if base >  sys.maxint / 10 or ((base == sys.maxint / 10) and (str[i] - '0' > 7)): 
                if sign == 1: 
                        return sys.maxint
                else:
                    return -sys.maxint-1
            
            base  = 10 * base + (ord(str[i]) - ord('0'))
            i+=1
        
        return base * sign
    