class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[] 
        # for i in range(len(asteroids)):
        
        i=0
        while i<len(asteroids):

            if asteroids[i]>0 or not stack or stack[len(stack)-1]<0:         
                stack.append(asteroids[i])
            elif stack[len(stack)-1]<= -asteroids[i]:
                
                if stack[len(stack)-1]< -asteroids[i]:
                    i-=1
                stack.pop()
            i+=1
        
        return stack