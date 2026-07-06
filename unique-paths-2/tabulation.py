class Solution:
    def uniquePathsWithObstacles(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dp = [[-1]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i >= 0 and j >= 0 and matrix[i][j] == 1:
                    dp[i][j] = 0

                elif i == 0 and j == 0:
                    dp[0][0] = 1
                
                else:
                    up = dp[i-1][j] if i > 0 else 0
                    left = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = up + left

        return dp[m-1][n-1]
    
# Time complexity: O(m*n)
# Space complexity: O(m*n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])) # return 2
    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 0, 1]])) # return 0
    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 1], [0, 1, 0]])) # return 0
    print(dummy.uniquePathsWithObstacles([[0, 0, 0, 0], [0, 0, 1, 0]])) # return 1