class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not str: #or len(s)==1:
            return False
                
        # ss = (s + s)[len(s)/2:-len(s)/2]
        ss = (s + s)[1:-1]
        return ss.find(s) != -1