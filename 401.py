class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def helper(lis, k):
            if k <= 0:
                return []
            if k == 1:
                return lis
            if k > len(lis):
                return []
            if k == len(lis):
                return [sum(lis)]
            ans = []
            for i in range(len(lis)):
                temp = helper(lis[i+1:], k-1)
                for v in temp:
                    ans.append(lis[i] + v)
            return ans
        
        if num == 0:
            return ['0:00']  
        
        hours = [1, 2, 4, 8]
        minutes = [1, 2, 4, 8, 16, 32]
        ans = []
        for i in range(max(0, num-5), min(num, 3)+1):
            h = [x for x in helper(hours, i) if 0 <= x <= 11] or [0]
            m = [x for x in helper(minutes, num-i) if 0 <= x <= 59] or [0]
            for j in range(len(h)):
                for k in range(len(m)):
                    ans.append('{}:{}'.format(h[j], str(m[k]).zfill(2)))
        return ans