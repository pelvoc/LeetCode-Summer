class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        if len(board)==0: return False
        if len(board[0])==0: return False
        
        visited=[[False for x in range(len(board[0]))] for y in range(len(board))]
    
        # print visited
    
        def helper(board, word, hr, hc, index): 

            if index==len(word):
                return True

            if hr<0  or hr>=len(board) or hc<0 or hc>=len(board[hr]) or board[r][c]!=word[index] or visited[r][c]: 
                return False
            
            
            visited[hr][hc]=True

            if (board, word, hr-1, hc, index+1) or \
               (board, word, hr+1, hc, index+1) or \
               (board, word, hr, hc-1, index+1) or \
               (board, word, hr, hc+1, index+1): 
                return True

            visited[hr][hc]=False
            return False
        
        for r in range(len(board)): 
            for c in range(len(board[r])):
                if (board[r][c]==word[0]) and helper(board, word, r, c, 0): 
                   return True
        
        return False