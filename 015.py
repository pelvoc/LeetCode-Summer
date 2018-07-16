class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """ 
        if nums==[0,0,0]:
            return [nums]

        res=[]
        nums.sort()
        
        for i in range(len(nums)):
            
            target=-nums[i]
            front=i+1
            back=len(nums)-1

            while front<back: 
                
                sums=nums[front]+nums[back]
                
                if sums<target:
                    front+=1
                elif sums>target:
                    back-=1
                else:
                    triplet=[0]*3
                    triplet[0]=nums[i]
                    triplet[1]=nums[front]
                    triplet[2]=nums[back]
                    res.append(triplet)
                    
                    while front<back and nums[front]==triplet[1]: 
                        front+=1
                    while front<back and nums[back]==triplet[2]:
                        back-=1
            while i+1<len(nums) and nums[i]==nums[i+1]: 
                i+=1
                
        # res=res[:-1]
                
        return res