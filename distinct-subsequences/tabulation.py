class Solution:
    # updated memoization for tabulation
    def foo(self, i, j, s, t, dp):
        if j == 0:
            return 1
        
        if i == 0:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
    
        if s[i-1] == t[j-1]:
            dp[i][j] = self.foo(i-1, j-1, s, t, dp) + self.foo(i-1, j, s, t, dp)
            return dp[i][j]
        
        dp[i][j] = self.foo(i-1, j, s, t, dp)
        return dp[i][j]

    def distinctSubsequences(self, s, t):
        n, m = len(s), len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(0, n+1):
            dp[i][0] = 1
        
        # we start from 1 here because we rewrite (0,0) which must be 1
        for j in range(1, m+1):
            dp[0][j] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][m]
          
# Time complexity: O(m*n)
# Space complexity: O(m*n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.distinctSubsequences("babgbag", "bag"))
    print(dummy.distinctSubsequences("axbxax", "axa"))
    print(dummy.distinctSubsequences("rabbbit", "rabbit"))