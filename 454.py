class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d=dict()     
        
        for i in range(len(C)):
            for j in range(len(D)):
                sums=C[i]+D[j]
                d[sums]=d.get(sums, 0)+1
                
        res=0
        for i in range(len(A)):
            for j in range(len(B)):
                target=-(A[i]+B[j])
                res+=d.get(target, 0)
                
        return res