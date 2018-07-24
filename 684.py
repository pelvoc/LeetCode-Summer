class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent=[0]*1001
        
        for i in range(len(parent)):
            parent[i]=i
        
        for edge in edges:
            f=edge[0]
            t=edge[1]
        
            if self.find(parent, f)==self.find(parent, t):
                return edge
            else: 
                parent[self.find(parent, f)]=self.find(parent, t)
        
    def find(self, parent, f): 
        if f!=parent[f]:
            parent[f]=self.find(parent, parent[f])
            
        return parent[f]