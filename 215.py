import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle (lst )
        k=len(nums)-k
        lo=0
        hi=len(nums)-1

        while lo<hi:
            j=self.partition(nums, lo, hi)
            if j<k:
                lo=j+1
            elif j>k:
                hi=j-1
            else: 
                break
                
        return nums[k]

    def partition(self, a, lo, hi):
        
        i=lo
        j=hi+1
        
        while True:
            while j<hi and a[i]
    
            while j>lo and a[lo]