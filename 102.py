import Queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        if not root:
            return []
        
        ans, level = [], [root]
        
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans
        """    
        q = Queue.Queue()
        wrapList=[[]]
        
        if root == None:
            return wrapList
    
        q.put(root)
        while not q.empty():
            levelNum=q.qsize()
            subList=[]
            for i in range(levelNum): 
                if not q[0].left : 
                    q.put(q.get(0).left)
                if not q[0].right: 
                    q.put(q.get(0).right)
                subList.append(q.poll().val)
                
            wrapList.append(subList)
        
        return wrapList