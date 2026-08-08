class Solution:
    def foo(self, i, j, matrix, dp):
        if j < 0 or j >= len(matrix[0]):
            return float("inf")

        if dp[i][j] != -1:
            return dp[i][j]

        if i == 0:
            return matrix[0][j]

        one = matrix[i][j] + self.foo(i-1, j-1, matrix, dp)
        two = matrix[i][j] + self.foo(i-1, j, matrix, dp)
        three = matrix[i][j] + self.foo(i-1, j+1, matrix, dp)

        dp[i][j] = min(one, two, three)
        return dp[i][j]

    def minPathSum(self, matrix):
        n, m = len(matrix), len(matrix[0])
        minSum = float("inf")
        dp = [[-1] * m for _ in range(n)]

        for j in range(len(matrix[0])):
            minSum = min(minSum, self.foo(n-1, j, matrix, dp))

        return minSum

# Time complexity: O(n*m)
# Space complexity: O(n) + O(n*m)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.minPathSum([[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]))
    print(dummy.minPathSum([[1, 4, 3, 1], [2, 3, -1, -1], [1, 1, -1, 8]]))
    print(dummy.minPathSum([[4, 3, 4], [4, 5, 1], [4, 6, 2], [4, 1, 4]]))