# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None: 
            return True
            
        return self.helper(root.left, root.right) and self.helper(root.right, root.left)
    
    
    def helper(self, left, right):
        
        if left==None or right==None:
            return left==right
        if left.val!=right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(right.left, left.right)