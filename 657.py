class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        v=0
        h=0
        
        for m in moves:
            if m=='U':
                v+=1
            if m=='D':
                v-=1
            if m=='L':
                h-=1
            if m=='R':
                h+=1
            
        return v==0 and h==0