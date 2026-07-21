class Solution:
    # updated memoization for tabulation
    def foo(self, i, j, pat, str, dp):
        if i == 0 and j == 0:
            return True

        if i == 0 and j > 0:
            return False
    
        if j == 0 and i > 0:
            for ii in range(1, i+1):
                if pat[ii-1] != '*':
                    return False
            return True
        
        if dp[i][j] != -1:
            return dp[i][j]
    
        if pat[i-1] == str[j-1] or pat[i-1] == '?':
            dp[i][j] = self.foo(i-1, j-1, pat, str, dp)
            return dp[i][j]

        if pat[i-1] == '*':
            dp[i][j] = self.foo(i-1, j, pat, str, dp) or self.foo(i, j-1, pat, str, dp)
            return dp[i][j]
        
        dp[i][j] = False
        return dp[i][j]
    
    def wildCard(self, str: str, pat: str) -> bool:
        n, m = len(pat), len(str) 
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True
        
        for j in range(1, m+1):
            dp[0][j] = False
        
        for i in range(1, n+1):
            flag = True
            for ii in range(1, i+1):
                if pat[ii-1] != '*':
                    flag = False
            dp[i][0] = flag
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if pat[i-1] == str[j-1] or pat[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]

                elif pat[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

                else:
                    dp[i][j] = False

        return dp[n][m]
    
# Time complexity: O(n*m)
# Space complexity: O(n*m)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.wildCard("abdefcd", "ab*cd"))
    print(dummy.wildCard("xaylmz", "x?y*z"))
    print(dummy.wildCard("xyza", "x*z"))
    print(dummy.wildCard("abc", "a**bc"))
    print(dummy.wildCard("a", "****"))