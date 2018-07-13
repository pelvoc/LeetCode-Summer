class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        if len(board)==0: return 0
        count = 0
        for r in range(len(board)): 
            for c in range(len(board[0])): 
                if board[r][c] == '.': continue
                if r>0 and board[r-1][c] == 'X': continue
                if c>0 and board[r][c-1] == 'X': continue
                count+=1
                
        return count