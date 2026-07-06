class Solution:
    def uniquePaths(self, m, n):
        dp = [[-1] * n for _ in range(m)]
        
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue 

                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0

                dp[i][j] = up + left
        
        return dp[m-1][n-1]
    
# Time complexity: O(m*n)
# Space complexity: O(m*n)

if __name__ == "__main__":
    dummy = Solution()
    
    print(dummy.uniquePaths(3, 2))
    print(dummy.uniquePaths(2, 4))