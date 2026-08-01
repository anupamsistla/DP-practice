from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*m for _ in range(n)]

        for i in range(n):
            dp[i][0] = matrix[i][0]

        for j in range(m):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

        for i in range(n):
            for j in range(m):
                res += dp[i][j]
        return res

# Time complexity: O(n * m)
# Space complexity: O(n * m) 

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.countSquares([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
    print(dummy.countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
    print(dummy.countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))