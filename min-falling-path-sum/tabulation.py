class Solution:
    def minPathSum(self, matrix):
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]

        for j in range(m):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(m-1, -1, -1):
                one = matrix[i][j] + dp[i-1][j-1] if j > 0 else float("inf")
                two = matrix[i][j] + dp[i-1][j]
                three = matrix[i][j] + dp[i-1][j+1] if j < m-1 else float("inf")
        
                dp[i][j] = min(one, two, three)

        minSum = float("inf")
        for j in range(len(matrix[0])):
            minSum = min(minSum, dp[n-1][j])

        return minSum

# Time complexity: O(n*m)
# Space complexity: O(n*m)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.minPathSum([[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]))
    print(dummy.minPathSum([[1, 4, 3, 1], [2, 3, -1, -1], [1, 1, -1, 8]]))
    print(dummy.minPathSum([[4, 3, 4], [4, 5, 1], [4, 6, 2], [4, 1, 4]]))