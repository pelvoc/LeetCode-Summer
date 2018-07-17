class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt=[0]*26
        pos=0 
        for i in range(len(s)): 
            cnt[ord(s[i])-ord('a')]+=1
        for i in range(len(s)): 
            # print s[i], "@@@@@@@@"
            if s[i]<s[pos]: 
                pos=i
            # print s[i], "0"
            # print cnt[ord(s[i])-ord('a')], "1"
            cnt[ord(s[i])-ord('a')]-=1
            if cnt[ord(s[i])-ord('a')]==0: 
                # print s[i]
                # print cnt[ord(s[i])-ord('a')], "2"
                # print cnt[ord(s[i])-ord('a')], "3"
                break
 
        return "" if len(s)==0 else s[pos]+self.removeDuplicateLetters(s[pos+1:]).replace(""+s[pos], "")
