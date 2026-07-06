class Solution:
    def foo(self, i, j, matrix, dp):
        if i >= 0 and j >= 0 and matrix[i][j] == 1:
            return 0
        
        if i == 0 and j == 0:
            return 1

        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]
        
        up = self.foo(i-1, j, matrix, dp)
        left = self.foo(i, j-1, matrix, dp)

        dp[i][j] = up + left
        return dp[i][j]
    
    def uniquePathsWithObstacles(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dp = [[-1]*n for _ in range(m)]
        return self.foo(m-1, n-1, matrix, dp)
    
# Time complexity: O(m*n)
# Space complexity: Path length = (m-1 + n-1) + (m*n) = O(m*n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])) # return 2
    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 0, 1]])) # return 0
    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 1], [0, 1, 0]])) # return 0
    print(dummy.uniquePathsWithObstacles([[0, 0, 0, 0], [0, 0, 1, 0]])) # return 1