# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxs=0
        self.maxDepth(root)
        
        return self.maxs
        
    def maxDepth(self, root):
        
        if root==None: 
            return 0
        
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        
        self.maxs=max(self.maxs, left+right)
        
        return max(left, right)+1