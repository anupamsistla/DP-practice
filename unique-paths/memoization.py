class Solution:
    def foo(self, i, j, dp):
        if i == 0 and j == 0:
            return 1
    
        if i < 0 or j < 0:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        up = self.foo(i-1, j, dp)
        left = self.foo(i, j-1, dp)
        
        dp[i][j] = up + left
        return dp[i][j]

    def uniquePaths(self, m, n):
        dp = [[-1] * n for i in range(m)]
        return self.foo(m-1, n-1, dp)

# Time complexity: O(m*n)
# Space complexity: Path length = (m-1 + n-1) + (m*n) = O(m*n)

if __name__ == "__main__":
    dummy = Solution()
    
    print(dummy.uniquePaths(3, 2))
    print(dummy.uniquePaths(2, 4))