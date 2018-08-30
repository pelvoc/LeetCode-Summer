class Solution(object):
    def countPalindromicSubsequences(self, S):
        N = len(S)
        A = [ord(c) - ord('a') for c in S]
        prv = [None] * N
        nxt = [None] * N
    
        last = [None] * 4
        for i in xrange(N):
            last[A[i]] = i
            prv[i] = tuple(last)
            
        last = [None] * 4
        for i in xrange(N-1, -1, -1):
            last[A[i]] = i
            nxt[i] = tuple(last)
        
        MOD = 10**9 + 7
        memo = [[None] * N for _ in xrange(N)]
        def dp(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            ans = 1 # The empty-string palindrome
            if i <= j:
                for x in xrange(4): # For letter a, b, c, d ...
                    i0 = nxt[i][x]
                    j0 = prv[j][x]
                    if i <= i0 <= j:
                        ans += 1 # The letter x exists in [i, j]
                    if None < i0 < j0:
                        ans += dp(i0+1, j0-1) # Counting palindromes "x_x"
            ans %= MOD
            memo[i][j] = ans
            return ans
        
        return dp(0, N-1) - 1 #Subtract empty string