class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        
        if m<n: 
            # return findMedianSortedArrays(nums2, nums1)
            nums1, nums2, m, n = nums2, nums1, n, m
            
        l, r = 0, n*2
        
        while l<=r: 
            mid2=(l+r)/2
            mid1=m+n-mid2
        
            l1 = -sys.maxint-1 if mid1==0 else nums1[(mid1-1)/2]
            l2 = -sys.maxint-1 if mid2==0 else nums2[(mid2-1)/2]
            r1 = sys.maxint if mid1==m*2 else nums1[mid1/2]
            r2 = sys.maxint if mid2==n*2 else nums2[mid2/2]
        
            if l1>r2: 
                l=mid2+1
            elif l2>r1: 
                r=mid2-1
            else:
                return (max(l1,l2)+min(r1,r2)) / 2.0
            
        return -1