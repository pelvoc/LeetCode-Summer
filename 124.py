# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxVal=-sys.maxint-1
        self.maxPathDown(root)
        
        return self.maxVal
        
    def maxPathDown(self, node): 
        if node==None: return 0
        l=max(0, self.maxPathDown(node.left))
        r=max(0, self.maxPathDown(node.right))
        self.maxVal=max(self.maxVal, l+r+node.val)
        
        return max(l, r)+node.val