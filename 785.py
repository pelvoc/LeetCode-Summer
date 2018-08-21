class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n=len(graph)     
        colors=[-1]*n
        
        for i in range(n):
            if colors[i]==-1 and not self.validColor(graph, colors, 0, i): 
                return False
        
        return True
        
    def validColor(self, graph, colors, color, node):
        
        if colors[node]!=-1:
            return colors[node]==color 
        
        colors[node]=color
        
        for next in graph[node]:
            if not self.validColor(graph, colors, 1-color, next):
                return False
        
        return True