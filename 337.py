# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=self.robSub(root)
        
        return max(res[0], res[1])
       
        
    def robSub(self, node): 
        
        if node==None: return [0]*2
        
        left=self.robSub(node.left)
        right=self.robSub(node.right)
        res=[0]*2
        
        res[0]=max(left[0], left[1])+max(right[0], right[1])
        res[1]=node.val+left[0]+right[0]
        
        return res