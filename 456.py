class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s3=-sys.maxint-1
        
        st=[]
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i]<s3:
                return True
            else: 
                while st and nums[i] > st[len(st)-1]: 
                    s3=st[len(st)-1]
                    st.pop()
            st.append(nums[i])
        
        return False