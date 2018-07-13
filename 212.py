class Solution(object):
    
    def findWords(self, board, words):
        
        self.res=[]
        trie=Trie()
        
        for w in words:
            trie.insert(w)
              
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for __ in range(m)]
        
        for r in range(m): 
            for c in range(n): 
                self.dfs(board, visited, '', r, c, trie)
    
        # self.res.sort()
        
        return self.res
        
    def dfs(self, board, visited, string, r, c, trie): 
        if r<0 or r>=len(board) or c<0 or c>=len(board[r]): return 

        if visited[r][c]: return

        string +=board[r][c]

        if not trie.startsWith(string): return

        if trie.search(string): self.res.append(string)

        visited[r][c]=True
        self.dfs(board, visited, string, r - 1, c, trie)
        self.dfs(board, visited, string, r + 1, c, trie)
        self.dfs(board, visited, string, r, c - 1, trie)
        self.dfs(board, visited, string, r, c + 1, trie)
        visited[r][c]=False    
        
#208. Implement Trie (Prefix Tree)
class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
      