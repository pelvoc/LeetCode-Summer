# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sums=0
        
        self.convert(root)
        return root
        
    def convert(self, cur):  #TreeNode cur
        if cur==None:
            return
        self.convert(cur.right)
        cur.val+=self.sums
        self.sums=cur.val
        self.convert(cur.left)