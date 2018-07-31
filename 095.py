# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0: return []
        
        return self.genTrees(1, n)
        
    def genTrees(self, start, end):
        
        ls=[]
        
        if start>end:
            ls.append(None)
            return ls
        
        if start==end:
            ls.append(TreeNode(start))
            return ls
    
        for i in range(start, end+1):
            
            left=self.genTrees(start, i-1)
            right=self.genTrees(i+1, end)
            
            for lnode in left: 
                for rnode in right: 
                    root=TreeNode(i)
                    root.left=lnode
                    root.right=rnode
                    ls.append(root)

        return ls