class Solution:
    def foo(self, i, j, s, t, dp):
        if j < 0:
            return 1
        
        if i < 0:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
    
        if s[i] == t[j]:
            dp[i][j] = self.foo(i-1, j-1, s, t, dp) + self.foo(i-1, j, s, t, dp)
            return dp[i][j]
        
        dp[i][j] = self.foo(i-1, j, s, t, dp)
        return dp[i][j]

    def distinctSubsequences(self, s, t):
        n, m = len(s), len(t)
        dp = [[-1] * m for _ in range(n)]
        return self.foo(n-1, m-1, s, t, dp)
          
# Time complexity: O(m*n)
# Space complexity: O(m*n) + O(m+n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.distinctSubsequences("babgbag", "bag"))
    print(dummy.distinctSubsequences("axbxax", "axa"))
    print(dummy.distinctSubsequences("rabbbit", "rabbit"))