class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res=[]
        if nums==None or len(nums)<4: return self.res
    
        nums.sort()
        
        maxVal=nums[len(nums)-1]
        if 4*nums[0]>target or 4*maxVal<target:
            return  self.res
        
        for i in range(len(nums)):
            z=nums[i]
            if i>0 and z==nums[i-1]: 
                continue
            if z+3*maxVal<target: 
                continue
            if 4*z>target: 
                break
            if 4*z==target:
                if i+3<len(nums) and nums[i+3]==z: 
                    self.res.append([z,z,z,z])
                break
                
            self.threeSum(nums, target-z, i+1, len(nums)-1, z)
    
        return self.res
        
        
    def threeSum(self, nums, target, l, r, z1): 
        
        if l+1>=r: return
        
        maxVal=nums[r]
        
        if 3*nums[l]>target or 3*nums[r]<target: 
            return
        
        for i in range(l, r-1):
            z=nums[i]
            if i>l and z==nums[i-1]: continue
            if z+2*maxVal<target: continue    
            if z*3>target: break
            if z*3==target: 
                if i+1<r and nums[i+2]==z: 
                    self.res.append([z1,z,z,z])
                break
                
            self.twoSum(nums, target-z, i+1, r, z1, z)

                
    def twoSum(self, nums, target, l, r, z1, z2): 
    
        if l>=r: return
        
        if 2*nums[l]>target or 2*nums[r]<target: return 
        
        i=l
        j=r
        while i<j:
            sums=nums[i]+nums[j]
            if sums==target:  
                self.res.append([z1, z2, nums[i], nums[j]])
                x=nums[i]
                while i+1<j and x==nums[i+1]:
                    i+=1
                x=nums[j]
                while i<j-1 and x==nums[j-1]: 
                    j-=1
            
            if sums<target: 
                i+=1
            if sums>target: 
                j-=1
        
        return