class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails=[0]*len(nums)
        size=0
        for n in nums: 
            l=0
            r=size
            while l!=r:
                mid=(l+r)/2
                if tails[mid]<n: 
                    l=mid+1
                else:
                    r=mid
            tails[l]=n       
            if l==size:
                size+=1
        
        return size