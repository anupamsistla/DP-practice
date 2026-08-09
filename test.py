class Solution:
    def foo(self, i, j, triangle, dp):
        if i == 0 and j == 0:
            return triangle[0][0]

        if j < 0:
            return float("inf")

        if dp[i][j] != -1:
            return dp[i][j]

        up = float("inf")

        if i != j:
            up = triangle[i][j] + self.foo(i-1, j, triangle, dp)

        upLeft = triangle[i][j] + self.foo(i-1, j-1, triangle, dp)
        dp[i][j] = min(up, upLeft)

        return dp[i][j]

    def minTriangleSum(self, triangle):
        n = len(triangle)
        m = len(triangle[n-1])
        prev = [0] * m

        minSum = float("inf")

        prev[0] = triangle[0][0]

        for i in range(1, n):
            curr = [0] * m
            for j in range(len(triangle[i])):
                up = float("inf")
                
                if i != j:
                    up = triangle[i][j] + prev[j]

                upLeft = triangle[i][j] + prev[j-1] if j > 0 else float("inf")
                curr[j] = min(up, upLeft)
            prev = curr

        for j in range(m):
            minSum = min(minSum, prev[j])
        return minSum

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minTriangleSum([[1], [1, 2], [1, 2, 4]]))
    print(dummy.minTriangleSum([[1], [4, 7], [4,10, 50], [-50, 5, 6, -100]]))
    