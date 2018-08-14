class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # if num<10: return num
        
        digits=[int(x) for x in str(num)]
        
        buckets=[0]*10
        
        # digits[0], digits[1]=digits[1], digits[0]
        
        for i in range(len(digits)):
            buckets[digits[i]]=i
        
        for i in range(len(digits)):
            for j in range(9, digits[i]-1, -1):
                if buckets[j]>i: 
                    digits[i], digits[buckets[j]]=digits[buckets[j]], digits[i]
                    
                    return self.magic(digits)
        
    def magic(self, numList):
        s = ''.join(map(str, numList))
        return int(s)