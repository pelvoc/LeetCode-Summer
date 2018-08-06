# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root==None: return None
        
        while root: 
            
            if p.val < root.val > q.val:
                root=root.left
            elif p.val > root.val < q.val:
                root=root.right
            else: # p.val < root.val < q.val:
                return root