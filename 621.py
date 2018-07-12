class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
 
        alphabet = [0] * 26

        for i in tasks: 
            alphabet[ord(i) - ord('A')] += 1 
        
        alphabet.sort()
        
        print alphabet
        
        i = 25
        while(i>=0 and alphabet[i]==alphabet[25]):
            i-=1
        
        return max(len(tasks),  (alphabet[25] - 1) * (n + 1) + (25 - i))
        